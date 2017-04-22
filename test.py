#!/usr/bin/env python
# encoding: utf-8
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:
这个只是一个用来测试的文件 并不是工程中的文件
"""
import tensorflow as tf


def test_expand_dim():
    vec = tf.constant([1, 1, 1, 1])
    sess = tf.Session()
    print sess.run(vec)