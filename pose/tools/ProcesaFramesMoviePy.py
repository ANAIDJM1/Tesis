from __future__ import print_function, unicode_literals

import tensorflow as tf
import numpy as np
import scipy.misc
import os
import sys
sys.path.append('/home/any/Imágenes/tesis/')
import argparse
import operator
import csv
import cv2
from moviepy.editor import VideoFileClip

from nets.ColorHandPose3DNetwork import ColorHandPose3DNetwork
from utils.general import detect_keypoints, trafo_coords, plot_hand, plot_hand_2d, plot_hand_3d
from pose.DeterminacionPosicion import *
from pose.utils.EstimacionposeDedo import EstimacionPoseDedo

# Variables a usar
image_tf = None
threshold = None
poses_dedo_conocidas = None
network_elements = None
output_txt_path = None
reqd_pose_name = None

def parse_args():
	parser = argparse.ArgumentParser(description = 'Procesa los frames de un video en particular')
	parser.add_argument('ruta_video', help = 'ruta del video', type = str)
	# This part needs improvement. Currently, pose_no is position_id present in FormaciondedatosDedos.py
	parser.add_argument('pose_no', help = 'Pose a clasificar', type = int)
	parser.add_argument('--output-path', dest = 'output_path', type = str, default = None,
						help = 'Ruta del folder donde se almacena el texto de salida')
	parser.add_argument('--thresh', dest = 'threshold', help = ' umbral de confianza (0-1)', default = 0.45,
	                    type = float)
	args = parser.parse_args()
	return args

"""Preparar rutas de entrada y de salida"""
def prepara_rutas(ruta_video, salida_txt_ruta):
	ruta_video = os.path.abspath(ruta_video)

	if salida_txt_ruta is None:
		salida_txt_ruta = os.path.split(ruta_video)[0]
	else:
		salida_txt_ruta = os.path.abspath(salida_txt_ruta)
		if not os.path.exists(salida_txt_ruta):
			os.mkdir(salida_txt_ruta)

	nombre_archivo = os.path.basename(ruta_video).split('.')[0]
	ruta_salida_video = os.path.join(salida_txt_ruta, '{}_procesado.mp4'.format(nombre_archivo))
	salida_txt_ruta = os.path.join(salida_txt_ruta, '{}.csv'.format(nombre_archivo))
	if not os.path.exists(salida_txt_ruta):
		open(salida_txt_ruta, 'w').close()
	return ruta_video, salida_txt_ruta, ruta_salida_video

def prepara_redCNN():
	# entrada de la red
	image_tf = tf.placeholder(tf.float32, shape = (1, 240, 320, 3))
	lado_mano_tf = tf.constant([[1.0, 1.0]])  #para incluir mano derecha e izquierda
	evaluation = tf.placeholder_with_default(True, shape = ())

	# construccion de red
	net = ColorHandPose3DNetwork()
	hand_scoremap_tf, image_crop_tf, scale_tf, center_tf,\
		keypoints_scoremap_tf, keypoint_coord3d_tf = net.inference(image_tf, lado_mano_tf, evaluation)

	# Inicia TF
	gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
	sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

	# initialize network
	net.init(sess)

	return sess, image_tf, keypoint_coord3d_tf, scale_tf, center_tf, keypoints_scoremap_tf

def procesa_video_frame(video_frame):
	video_frame = video_frame[:, :, :3]
	video_frame = scipy.misc.imresize(video_frame, (240, 320))
	image_v = np.expand_dims((video_frame.astype('float') / 255.0) - 0.5, 0)

	keypoint_coord3d_tf, scale_tf, center_tf, keypoints_scoremap_tf = network_elements
	keypoint_coord3d_v, scale_v, center_v, keypoints_scoremap_v = sess.run([keypoint_coord3d_tf,
		scale_tf, center_tf, keypoints_scoremap_tf], feed_dict = {image_tf: image_v})

	keypoints_scoremap_v = np.squeeze(keypoints_scoremap_v)
	keypoint_coord3d_v = np.squeeze(keypoint_coord3d_v)

	# post procesamiento
	coord_hw_crop = detect_keypoints(np.squeeze(keypoints_scoremap_v))
	coord_hw = trafo_coords(coord_hw_crop, center_v, scale_v, 256)

	plot_hand_2d(coord_hw, video_frame)

	score_label = procesamiento_keypoints(keypoint_coord3d_v)
	if score_label is not None:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(video_frame, score_label, (10, 200), font, 1.0, (255, 0, 0), 2, cv2.LINE_AA)
		
	return video_frame

def procesamiento_keypoints(keypoint_coord3d_v):
	Estiacion_poseDedo = EstimacionPoseDedo(keypoint_coord3d_v)
	Estiacion_poseDedo.calcular_posicion_dedos(print_finger_info = False)
	obtained_positions = determinar_posicion(Estiacion_poseDedo.Curvatura_dedo,
											 Estiacion_poseDedo.posicion_dedo, poses_dedo_conocidas,
											 threshold)

	score_label = None
	if len(obtained_positions) > 0:
		max_pose_label = max(obtained_positions.items(), key=operator.itemgetter(1))[0]
		if obtained_positions[max_pose_label] >= threshold and max_pose_label == reqd_pose_name:
			score_label = max_pose_label
			with open(output_txt_path, 'a') as fid:
				list_entry = [entry for sublist in keypoint_coord3d_v for entry in sublist]
				csv_writer = csv.writer(fid)
				csv_writer.writerow(list_entry)
	
	return score_label

if __name__ == '__main__':
	args = parse_args()
	threshold = args.threshold * 10
	ruta_video, output_txt_path, output_video_path = prepara_rutas(args.ruta_video, args.output_path)
	poses_dedo_conocidas = crear_poses_conocidasDedos()
	reqd_pose_name = get_nombrePosicion_id(args.pose_no, poses_dedo_conocidas)
								
	sess, image_tf, keypoint_coord3d_tf, scale_tf, center_tf, keypoints_scoremap_tf = prepara_redCNN()
	network_elements = [keypoint_coord3d_tf, scale_tf, center_tf, keypoints_scoremap_tf]

	video_clip = VideoFileClip(ruta_video)
	white_clip = video_clip.fl_image(procesa_video_frame) #NOTA: esta función espera imágenes en color!!
	white_clip.write_videofile(output_video_path, audio=False) 
