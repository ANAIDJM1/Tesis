#
#  ColorHandPose3DNetwork - Network for estimating 3D Hand Pose from a single RGB Image
#  Copyright (C) 2017  Christian Zimmermann
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import print_function, unicode_literals

import tensorflow as tf
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from nets.ColorHandPose3DNetwork import ColorHandPose3DNetwork
from utils.general import detect_keypoints, trafo_coords, plot_hand, plot_hand_3d

if __name__ == '__main__':
    # images to be shown
    image_list = list()

    """" DATASET3
    image_list.append('./data/dataset3/a.jpg')
    image_list.append('./data/dataset3/b.jpg')
    image_list.append('./data/dataset3/c.jpg')
    image_list.append('./data/dataset3/d.jpg')
    image_list.append('./data/dataset3/e.jpg')
    image_list.append('./data/dataset3/f.jpg')
    image_list.append('./data/dataset3/g.jpg')
    image_list.append('./data/dataset3/h.jpg')
    image_list.append('./data/dataset3/i.jpg')
    image_list.append('./data/dataset3/k.jpg')
    image_list.append('./data/dataset3/l.jpg')
    image_list.append('./data/dataset3/m.jpg')
    image_list.append('./data/dataset3/n.jpg')
    image_list.append('./data/dataset3/o.jpg')
    image_list.append('./data/dataset3/p.jpg')
    image_list.append('./data/dataset3/q.jpg')
    image_list.append('./data/dataset3/r.jpg')
    image_list.append('./data/dataset3/s.jpg')
    image_list.append('./data/dataset3/t.jpg')
    image_list.append('./data/dataset3/u.jpg')
    image_list.append('./data/dataset3/v.jpg')
    image_list.append('./data/dataset3/w.jpg')
    image_list.append('./data/dataset3/x.jpg')
    image_list.append('./data/dataset3/y.jpg')"""

    """         DATASET1
    image_list.append('./data/dataset1/d.jpg')
    image_list.append('./data/dataset1/k.jpg')
    image_list.append('./data/dataset1/l.jpg')
    image_list.append('./data/dataset1/m.jpg')
    image_list.append('./data/dataset1/r.jpg')
    image_list.append('./data/dataset1/v.jpg')
    image_list.append('./data/dataset1/x.jpg')"""

    """DATASET 2"""
    image_list.append('./data/dataset2/d.jpg')
    image_list.append('./data/dataset2/k.jpg')
    image_list.append('./data/dataset2/l.jpg')
    image_list.append('./data/dataset2/v.jpg')
    image_list.append('./data/dataset2/x.jpg')



    # network input
    image_tf = tf.placeholder(tf.float32, shape=(1, 240, 320, 3))
    hand_side_tf = tf.constant([[1.0, 0.0]])  # left hand (true for all samples provided)
    evaluation = tf.placeholder_with_default(True, shape=())

    # build network
    net = ColorHandPose3DNetwork()
    hand_scoremap_tf, image_crop_tf, scale_tf, center_tf,\
    keypoints_scoremap_tf, keypoint_coord3d_tf = net.inference(image_tf, hand_side_tf, evaluation)

    # Start TF
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    # initialize network
    net.init(sess)

    # Feed image list through network
    for img_name in image_list:
        image_raw = scipy.misc.imread(img_name)
        image_raw = scipy.misc.imresize(image_raw, (240, 320))
        image_v = np.expand_dims((image_raw.astype('float') / 255.0) - 0.5, 0)

        hand_scoremap_v, image_crop_v, scale_v, center_v,\
        keypoints_scoremap_v, keypoint_coord3d_v = sess.run([hand_scoremap_tf, image_crop_tf, scale_tf, center_tf,
                                                             keypoints_scoremap_tf, keypoint_coord3d_tf],
                                                            feed_dict={image_tf: image_v})

        hand_scoremap_v = np.squeeze(hand_scoremap_v)
        image_crop_v = np.squeeze(image_crop_v)
        keypoints_scoremap_v = np.squeeze(keypoints_scoremap_v)
        keypoint_coord3d_v = np.squeeze(keypoint_coord3d_v)

        # post processing
        image_crop_v = ((image_crop_v + 0.5) * 255).astype('uint8')
        coord_hw_crop = detect_keypoints(np.squeeze(keypoints_scoremap_v))
        coord_hw = trafo_coords(coord_hw_crop, center_v, scale_v, 256)

        # visualize
        fig = plt.figure(1)
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224, projection='3d')
        ax1.imshow(image_raw)
        plot_hand(coord_hw, ax1)
        ax2.imshow(image_crop_v)
        plot_hand(coord_hw_crop, ax2)
        ax3.imshow(np.argmax(hand_scoremap_v, 2))
        plot_hand_3d(keypoint_coord3d_v, ax4)
        ax4.view_init(azim=-90.0, elev=-90.0)  # aligns the 3d coord with the camera view
        ax4.set_xlim([-3, 3])
        ax4.set_ylim([-3, 1])
        ax4.set_zlim([-3, 3])
        plt.show()
