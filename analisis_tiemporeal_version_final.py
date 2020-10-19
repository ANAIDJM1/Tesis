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
import time
import pickle
import glob

from nets.ColorHandPose3DNetwork import ColorHandPose3DNetwork
from utils.general import detect_keypoints, trafo_coords, plot_hand, plot_hand_2d, plot_hand_3d
from pose.DeterminacionPosicion import crear_poses_conocidasDedos, determinar_posicion, get_nombrePosicion_id
from pose.utils.EstimacionposeDedo import EstimacionPoseDedo


def parse_args():
    parser = argparse.ArgumentParser(
        description='Clasificacion de los gestos de manos desde el dataset de imagenes en el folder test_data')

    parser.add_argument('--plot-fingers', dest='plot_fingers', help='plotear dedos.(1 = si, 0 = No)',
                        default=1, type=int)
    parser.add_argument('--thresh', dest='threshold', help='Umbral de nivel de confianza(0-1)', default=0.45,
                        type=float)
    parser.add_argument('--solve-by', dest='solve_by', default=0, type=int,
                        help='Metodo para hacer el calculo: (0=Geometria, 1=Red Neuronal)')
    #Si se resuelve por red neuronal se entrega la ruta de los graficos pb-file
    parser.add_argument('--pb-file', dest='pb_file', type=str, default=None,
                        help='Ruta donde el grafico de la CNN se guarda.')

    args = parser.parse_args()
    return args


def prepara_entrada(ruta_entrada, ruta_salida):
    # ruta del destino de las imagenes
    ruta_entrada = os.path.abspath(ruta_entrada)
    # archivos dentro de la carpeta
    data_archivos = os.listdir(ruta_entrada)
    data_archivos = [os.path.join(ruta_entrada, data_a) for data_a in data_archivos]

    # si la ruta de salida no se da, se va guardar en el mismo folder de entrada
    if ruta_salida is None:
        ruta_salida = ruta_entrada
    else:
        ruta_salida = os.path.abspath(ruta_salida)

    # bota los archivos dentro de la carpeta y la ruta de salida
    return data_archivos, ruta_salida

#Prediccion por geometria
def prediccion_por_geometria(keypoint_coord3d_v, poses_dedo_conocidas, threshold):
    EsimacionDedoPose = EstimacionPoseDedo(keypoint_coord3d_v)
    EsimacionDedoPose.calcular_posicion_dedos(print_finger_info=True)
    posiciones_obtenidas = determinar_posicion(EsimacionDedoPose.Curvatura_dedo,
                                               EsimacionDedoPose.posicion_dedo, poses_dedo_conocidas,
                                               threshold * 10)

    etiqueta_score = 'Indefinido'
    if len(posiciones_obtenidas) > 0:
        max_pose_label = max(posiciones_obtenidas.items(), key=operator.itemgetter(1))[0]
        if posiciones_obtenidas[max_pose_label] >= threshold:
            etiqueta_score = max_pose_label

    print(posiciones_obtenidas)
    return etiqueta_score

# prediccion por la red neuronal (esta parte viene definida por la red de Zimmermann)
def predic_por_CNN(keypoint_coord3d_v, known_finger_poses, pb_file, threshold):
    detection_graph = tf.Graph()
    etiqueta_score = 'Indefinido'
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
            etiqueta_score = 'Indefinido' if score_index == -1 else get_nombrePosicion_id(score_index,
                                                                                                known_finger_poses)
            print(outputs)
    return etiqueta_score


if __name__ == '__main__':

    args = parse_args()

    """capturar el frame y ponerlo en el path, guardarlo, y final mostrar el frame procesado, 
    borrar contenido carpetas"""


    count=0
    #tiempo que aparece la ventana para leer la senha en segundos
    tiempo=8
    #empieza la cuenta
    inicio_tiempo=time.time()
    # captura webcam
    video_captura = cv2.VideoCapture(0)

    while(True):

        #toma tiempo actual
        tiempo_presente=time.time()
        # Captura frame-por-frame
        ret, frame = video_captura.read()

        #guarda el frame capturado por la webcam
        cv2.imwrite("./pose/test_data/frame%d.jpg" % count,frame)
        count+=1
        tiempo_pasa = tiempo_presente - inicio_tiempo

        # muestra el resultado del frame v2.imshow(window_name, image)
        cv2.imshow('Resultado de senia', frame)
        #
        if cv2.waitKey(1) & (tiempo_pasa > tiempo):
            break
    # cuando too esta hecho, libera y destruye ventana
    video_captura.release()
    cv2.destroyAllWindows()

    data_path='./pose/test_data/'
    data_path2 = './pose/test_data_salida/'

    data_files, output_path = prepara_entrada(data_path, data_path2)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    known_finger_poses = crear_poses_conocidasDedos()

    # ENTRADA DE RED
    image_tf = tf.placeholder(tf.float32, shape=(1, 240, 320, 3))
    hand_side_tf = tf.constant([[1.0, 1.0]])  # Both left and right hands included
    evaluation = tf.placeholder_with_default(True, shape=())

    # CONSTRUCCION DE RED
    net = ColorHandPose3DNetwork()
    hand_scoremap_tf, image_crop_tf, scale_tf, center_tf, \
    keypoints_scoremap_tf, keypoint_coord3d_tf = net.inference(image_tf, hand_side_tf, evaluation)

    # Inicia TF
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    # INICIA RED CNN
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

            # post procesamiento
            coord_hw_crop = detect_keypoints(np.squeeze(keypoints_scoremap_v))
            coord_hw = trafo_coords(coord_hw_crop, center_v, scale_v, 256)

            plot_hand_2d(coord_hw, image_raw)

        else:
            keypoint_coord3d_v = sess.run(keypoint_coord3d_tf, feed_dict={image_tf: image_v})

        # Clasificacion basada en el algoritmo de SVM
        if args.solve_by == 1:
            score_label = predic_por_CNN(keypoint_coord3d_v, known_finger_poses,
                                         args.pb_file, args.threshold)
        elif args.solve_by == 0:
            score_label = prediccion_por_geometria(keypoint_coord3d_v, known_finger_poses, args.threshold)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image_raw, score_label, (10, 200), font, 1.0, (255, 0, 0), 2, cv2.LINE_AA)

        file_name = os.path.basename(img_name)
        file_name_comp = file_name.split('.')
        file_save_path = os.path.join(output_path, "{}_salida.jpg".format(file_name_comp[0]))
        mpimg.imsave(file_save_path, image_raw)


    #--------------------------------------------------------//-------------------------------------
    #volver video las imagenes y reproducir el video
    img_array = []
    for imagenesprocesadas in glob.glob('./pose/test_data_salida/*.jpg'):
        img = cv2.imread(imagenesprocesadas)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    # guardar video en video_procesado
    out = cv2.VideoWriter('./pose/video_procesado/video_final.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    #-----------------------------------

    # Reproduce video procesado
    cap2 = cv2.VideoCapture('./pose/video_procesado/video_final.mp4')
    if (cap2.isOpened() == False):
        print("Error , no se puede abrir el video")
    while (cap2.isOpened()):
        ret, frame2 = cap2.read()
        if ret == True:
            cv2.imshow('Video de salida', frame2)
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        else:
            break

    cap2.release()
    cv2.destroyAllWindows()

    #limpiar la carpeta de entrada y de salida
    #borrar elementos de pose/test_data
    fotos1 = glob.glob('./pose/test_data/*')
    for f in fotos1:
        os.remove(f)
    #borrar elementos de pose/test_data_salida
    #fotos2 = glob.glob('./pose/test_data_salida/*')
    #for f2 in fotos2:
    #    os.remove(f2)


