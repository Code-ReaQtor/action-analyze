#!/usr/bin/env python
# encoding: utf-8
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:
"""

import tensorflow as tf


def get_data():
    """
    
    :return: 
    """
    pass
    return {}


def soft_max():
    x = tf.placeholder(tf.float32, [None, 61])

    # 程序的分类现在先不能确定，今天晚上大概还需要在确定下,先以7类为准

    W = tf.Variable(tf.zeros([61, 7]))
    b = tf.Variable(tf.zeros(7))

    y = tf.nn.softmax(tf.matmul(x, W) + b)

    #损失函数

    y_ = tf.placeholder(tf.float32, [None, 7])
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    #初始化
    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    data = get_data()
    for (batch_xs, batch_ys) in data.items():
        #
        # batch_xs, batch_ys = next_batch()
        sess.run(train_step, feed_dict={x:batch_xs, y_:batch_ys})


if __name__ == '__main__':
    soft_max()
