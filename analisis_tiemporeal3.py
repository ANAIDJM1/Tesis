from __future__ import print_function, unicode_literals

import tensorflow as tf
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys
PATH = ('/home/any/Imágenes/tesis')
from mpl_toolkits.mplot3d import Axes3D
import argparse
import cv2
import operator
import pickle

from nets.ColorHandPose3DNetwork import ColorHandPose3DNetwork
from utils.general import detect_keypoints, trafo_coords, plot_hand, plot_hand_2d, plot_hand_3d
from pose.DeterminacionPosicion import create_known_finger_poses, determine_position, get_position_name_with_pose_id
from pose.utils.EstimacionposeDedo import FingerPoseEstimate


def parse_args():
    parser = argparse.ArgumentParser(
        description='Clasificacion de los gestos de manos desde el dataset de imagenes en el folder')
    #parser.add_argument('data_path', help=' Ruta del folder que contiene las imagenes', type=str)
    #parser.add_argument('--output-path', dest='output_path', type=str, default=None,
                        #help='Path of folder where to store the evaluation result')
    parser.add_argument('--plot-fingers', dest='plot_fingers', help='plotear dedos.(1 = si, 0 = No)',
                        default=1, type=int)
    # Threshold is used for confidence measurement of Geometry and Neural Network methods
    parser.add_argument('--thresh', dest='threshold', help='Umbral de nivel de confianza(0-1)', default=0.45,
                        type=float)
    parser.add_argument('--solve-by', dest='solve_by', default=0, type=int,
                        help='Metodo para usar la CNN 3DHAND: (0=Geometry, 1=Neural Network, 2=SVM)')
    # If solving by neural network, give the path of PB file.
    parser.add_argument('--pb-file', dest='pb_file', type=str, default=None,
                        help='Ruta donde el grafico de la CNN se guarda.')

    args = parser.parse_args()
    return args


def prepare_input(data_path, output_path):
    # ruta del destino de las imagenes
    data_path = os.path.abspath(data_path)
    # archivos dentro de la carpeta
    data_files = os.listdir(data_path)
    data_files = [os.path.join(data_path, data_file) for data_file in data_files]

    # si la ruta de salida no se da, se va guardar en el mismo folder de entrada
    if output_path is None:
        output_path = data_path
    else:
        output_path = os.path.abspath(output_path)

    # bota los archivos dentro de la carpeta y la ruta de salida
    return data_files, output_path

#Prediccion por geometria
def predict_by_geometry(keypoint_coord3d_v, known_finger_poses, threshold):
    fingerPoseEstimate = FingerPoseEstimate(keypoint_coord3d_v)
    fingerPoseEstimate.calculate_positions_of_fingers(print_finger_info=True)
    obtained_positions = determine_position(fingerPoseEstimate.finger_curled,
                                            fingerPoseEstimate.finger_position, known_finger_poses,
                                            threshold * 10)

    score_label = 'Indefinido'
    if len(obtained_positions) > 0:
        max_pose_label = max(obtained_positions.items(), key=operator.itemgetter(1))[0]
        if obtained_positions[max_pose_label] >= threshold:
            score_label = max_pose_label

    print(obtained_positions)
    return score_label

# prediccion por la red neuronal
def predict_by_neural_network(keypoint_coord3d_v, known_finger_poses, pb_file, threshold):
    detection_graph = tf.Graph()
    score_label = 'Indefinido'
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(pb_file, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        with tf.Session(graph=detection_graph) as sess:
            input_tensor = detection_graph.get_tensor_by_name('input:0')
            output_tensor = detection_graph.get_tensor_by_name('output:0')

            flat_keypoint = np.array([entry for sublist in keypoint_coord3d_v for entry in sublist])
            flat_keypoint = np.expand_dims(flat_keypoint, axis=0)
            outputs = sess.run(output_tensor, feed_dict={input_tensor: flat_keypoint})[0]

            max_index = np.argmax(outputs)
            score_index = max_index if outputs[max_index] >= threshold else -1
            score_label = 'Indefinido' if score_index == -1 else get_position_name_with_pose_id(score_index,
                                                                                                known_finger_poses)
            print(outputs)
    return score_label


if __name__ == '__main__':

    args = parse_args()

    """capturar el frame y ponerlo en el path, guardarlo, y final mostrar el frame procesado, 
    borrar """

    #limpiarcarpeta de imagenes pre y post procesamiento
    video_captura = cv2.VideoCapture(0)
    count=0

    while (True):
        # Captura frame-por-frame
        ret, frame = video_captura.read()

        cv2.imwrite("./pose/test_data/frame%d.jpg" % count,frame)
        count+=1

        # muestra el resultado del frame v2.imshow(window_name, image)
        cv2.imshow('Resultado de senias', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_captura.release()
    cv2.destroyAllWindows()

    data_path='./pose/test_data/'

    data_files, output_path = prepare_input(data_path, data_path)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    known_finger_poses = create_known_finger_poses()

    # network input
    image_tf = tf.placeholder(tf.float32, shape=(1, 240, 320, 3))
    hand_side_tf = tf.constant([[1.0, 1.0]])  # Both left and right hands included
    evaluation = tf.placeholder_with_default(True, shape=())

    # build network
    net = ColorHandPose3DNetwork()
    hand_scoremap_tf, image_crop_tf, scale_tf, center_tf, \
    keypoints_scoremap_tf, keypoint_coord3d_tf = net.inference(image_tf, hand_side_tf, evaluation)

    # Start TF
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    # initialize network
    net.init(sess)

    # Alimenta la imagen a  travez de la red -  procesa la imagen
    for img_name in data_files:
        image_raw = scipy.misc.imread(img_name)[:, :, :3]
        image_raw = scipy.misc.imresize(image_raw, (240, 320))
        image_v = np.expand_dims((image_raw.astype('float') / 255.0) - 0.5, 0)

        if args.plot_fingers == 1:
            scale_v, center_v, keypoints_scoremap_v, \
            keypoint_coord3d_v = sess.run([scale_tf, center_tf, keypoints_scoremap_tf, \
                                               keypoint_coord3d_tf], feed_dict={image_tf: image_v})

            keypoints_scoremap_v = np.squeeze(keypoints_scoremap_v)
            keypoint_coord3d_v = np.squeeze(keypoint_coord3d_v)

            # post processing
            coord_hw_crop = detect_keypoints(np.squeeze(keypoints_scoremap_v))
            coord_hw = trafo_coords(coord_hw_crop, center_v, scale_v, 256)

            plot_hand_2d(coord_hw, image_raw)

        else:
            keypoint_coord3d_v = sess.run(keypoint_coord3d_tf, feed_dict={image_tf: image_v})

        # Clasificacion basada en CNN
        if args.solve_by == 1:
            score_label = predict_by_neural_network(keypoint_coord3d_v, known_finger_poses,
                                                        args.pb_file, args.threshold)
        elif args.solve_by == 0:
            score_label = predict_by_geometry(keypoint_coord3d_v, known_finger_poses, args.threshold)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_raw, score_label, (10, 200), font, 1.0, (255, 0, 0), 2, cv2.LINE_AA)

        file_name = os.path.basename(img_name)
        file_name_comp = file_name.split('.')
        file_save_path = os.path.join(output_path, "{}_salida.jpg".format(file_name_comp[0]))
        mpimg.imsave(file_save_path, image_raw)

        #arreglar la carpeta de salida
        #reproducir imagenes como video o convertir a video



