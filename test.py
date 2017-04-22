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
    vec2 = tf.Variable(vecs)
    ex_vec = tf.expand_dims(vec, 0)
    ex_vec2 = tf.expand_dims(vec2, 1)
    diff = tf.subtract(ex_vec, ex_vec2)
    sqr = tf.square(diff)
    distance = tf.reduce_sum(sqr, 2)

    assignments = tf.argmin(distance, 0)

    # 模拟计算图心
    # means = tf.concat(0, [tf.reduce_mean(tf.gather(vec, tf.reshape(tf.where(tf.equal(assignments, [1, 2])), [1, -1])), reduction_indices=[1])])
    # update_centroides = tf.assign(vecs, means)

    vec_1 = tf.constant([1, 2, 3, 4])
    equal_result = tf.equal(vec_1, [1 ,2, 3, 4])

    init_op = tf.initialize_all_variables()

    sess = tf.Session()
    sess.run(init_op)
    print sess.run(vec)
    print " ++++++++++ "
    print sess.run(ex_vec)
    print " ++++++++++ "
    print sess.run(distance)
    print " ++++++++++ /n assignments"
    print sess.run(assignments)
    print sess.run(tf.equal(assignments, [1, 2]))
    print " ++++++++++ "
    # print sess.run(update_centroides)
    print sess.run(equal_result)

if __name__ == "__main__":
    test_expand_dim()