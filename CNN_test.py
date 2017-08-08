#!/usr/bin/env python
# encoding: utf-8
"""
@author:fayren
@date:2017/7/29
@DESC:
"""

import tensorflow as tf


def test_tf():
    a = tf.placeholder("float")
    b = tf.placeholder("float")
    y = tf.multiply(a, b)
    sess = tf.Session()
    print sess.run(y, feed_dict={a: 3, b: 3})


if __name__ == "__main__":
    test_tf()