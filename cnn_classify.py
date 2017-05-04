#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: cnn_classify.py
@time: 2017/4/27 20:00
"""

import sys
import tensorflow as tf
import json


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def main():
    """
    
    :return: 
    """
    #
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])

    # conv layer-1
    x = tf.placeholder(tf.float32, [None, 784])
    x_image = tf.reshape(x, [-1, 28, 28, 1])

    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    

    return 0


if __name__ == '__main__':
    sys.exit(main())

