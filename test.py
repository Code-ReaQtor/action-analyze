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
    vec = tf.constant([[1, 1], [-1, -1]])
    vecs = [
        [1, 1],
        [2, 2],
        [3, 3]
    ]
    vec2 = tf.Variable(tf.slice(tf.random_shuffle(vecs), [0, 0], [2, -1]))
    ex_vec = tf.expand_dims(vec, 0)
    ex_vec2 = tf.expand_dims(vec2, 1)
    result = tf.subtract(vec, vec2)
    sess = tf.Session()
    print sess.run(result)


if __name__ == "__main__":
    test_expand_dim()