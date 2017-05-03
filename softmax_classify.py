#!/usr/bin/env python
# encoding: utf-8
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:
"""

import tensorflow as tf


def softmax():
    x = tf.placeholder(tf.float32, [None, 61])

    # 程序的分类现在先不能确定，今天晚上大概还需要在确定下,先以10类为准
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros(10))

    y = tf.nn.softmax(tf.matmul(x, W) + b)

    #损失函数
    y_ = tf.placeholder(tf.float32, [None, 10])
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    #初始化
    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    for i in range(1000):
        #
        # batch_xs, batch_ys = next_batch()
        sess.run(train_step, feed_dict={x:batch_xs, y_:batch_ys})



if __name__ == '__main__':
    softmax()
