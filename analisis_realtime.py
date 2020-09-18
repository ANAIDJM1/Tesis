from __future__ import print_function, unicode_literals

import parser
import tensorflow as tf
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys
PATH=('/home/any/Imágenes/tesis')
from mpl_toolkits.mplot3d import Axes3D
import argparse
import cv2
import operator
import pickle

from nets.ColorHandPose3DNetwork import ColorHandPose3DNetwork
from utils.general import detect_keypoints, trafo_coords, plot_hand, plot_hand_2d, plot_hand_3d
from pose.DeterminacionPosicion import create_known_finger_poses, determine_position, get_position_name_with_pose_id
from pose.utils.EstimacionposeDedo import FingerPoseEstimate
from evaluate_pose import predict_by_neural_network

"""def parse_args():
    parser = argparse.ArgumentParser(
        description='Clasificacion de los gestos de manos desde el dataset de imagenes en el folder')
    parser.add_argument('--plot-fingers', dest='plot_fingers', help='Should fingers be plotted.(1 = Yes, 0 = No)',
                        default=1, type=int)
    # Threshold is used for confidence measurement of Geometry and Neural Network methods
    parser.add_argument('--thresh', dest='threshold', help=' Umbral de confianza entre (0-1)', default=0.45,
                        type=float)
    parser.add_argument('--solve-by', dest='solve_by', default=0, type=int,
                        help='Solve the keypoints of Hand3d by which method: (0=Geometry, 1=Neural Network, 2=SVM)')
    # If solving by neural network, give the path of PB file.
    parser.add_argument('--pb-file', dest='pb_file', type=str, default=None,
                        help='Ruta donde la CNN en grafico se guarda.')

    args = parser.parse_args()
    return args"""

    #----------------------------------------------------------------------------------------------------------


# el main invoca a las funciones def
if __name__ == '__main__':
#args = parse_args()

# abre la camara
    video_captura = cv2.VideoCapture(0)


    while(True):
        # Captura frame-por-frame
        ret, frame = video_captura.read()

    # =======================================TOOOOOOOOODAS LAS OPERACION CON EL FRAM VIENEN AQUI================================


        known_finger_poses = create_known_finger_poses()

    # network input
        image_tf = tf.placeholder(tf.float32, shape=(1, 240, 320, 3))
        hand_side_tf = tf.constant([[1.0, 1.0]])  # Both left and right hands included
        evaluation = tf.placeholder_with_default(True, shape=())

    # build network
        net = ColorHandPose3DNetwork()
        hand_scoremap_tf, image_crop_tf, scale_tf, center_tf, \
        keypoints_scoremap_tf, keypoint_coord3d_tf = net.inference(image_tf, hand_side_tf, evaluation)

    # Inicia TF
        """gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    # inicializa red
        net.init(sess)


    # alimenta la lista de imagenes a traves de la red
        image_raw = scipy.misc.imresize(frame, (240, 320))
        image_v = np.expand_dims((image_raw.astype('float') / 255.0) - 0.5, 0)


        scale_v, center_v, keypoints_scoremap_v, \
        keypoint_coord3d_v = sess.run([scale_tf, center_tf, keypoints_scoremap_tf, \
                                               keypoint_coord3d_tf], feed_dict={image_tf: image_v})

        keypoints_scoremap_v = np.squeeze(keypoints_scoremap_v)
        keypoint_coord3d_v = np.squeeze(keypoint_coord3d_v)

    # post procesamiento
        coord_hw_crop = detect_keypoints(np.squeeze(keypoints_scoremap_v))
        coord_hw = trafo_coords(coord_hw_crop, center_v, scale_v, 256)

        plot_hand_2d(coord_hw, image_raw)


    # clasifica basado en la red Neuronal
        pb_file='./pose/learned_models/graph.pb'
        threshold=0.45
        score_label = predict_by_neural_network(keypoint_coord3d_v, known_finger_poses,
                                                        pb_file, threshold)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_raw, score_label, (10, 200), font, 1.0, (255, 0, 0), 2, cv2.LINE_AA)


        #file_name = os.path.basename(frame)
        #file_name_comp = file_name.split('.')
        #file_save_path = os.path.join(output_path, "{}_out.png".format(file_name_comp[0]))
        #mpimg.imsave(file_save_path, image_raw)"""

        #print('{} -->  {}\n\n'.format('imagen exitosa', score_label))




# muestra el resultado del frame v2.imshow(window_name, image)
        cv2.imshow('Resultado de senias',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# cuando too esta hecho, libera y destruye ventana
    video_captura.release()
    cv2.destroyAllWindows()