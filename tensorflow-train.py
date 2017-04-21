#/usr/bin/python
#coding=utf-8
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:
使用tensorflow 实现特征行为聚类。
"""
import tensorflow as tf
import sys
import json
from numpy import array


def test_tf():
    a = tf.placeholder("float")
    b = tf.placeholder("float")
    y = tf.multiply(a, b)
    sess = tf.Session()
    print sess.run(y, feed_dict={a: 3, b: 3})


def input_mtx():
    """
    加载文件中保存的矩阵，转换成输入。进行聚类
    :return: 返回文件中的向量
    """
    mtx_file = open("data/vector_file.json", 'r')
    #　加载向量
    vec_dict = json.load(mtx_file)
    vectors = []
    for value in vec_dict:
        vectors.append(value)
    mtx_file.close()

    print u"加载向量文件完成"
    return vectors


def tf_train():
    """
    使用tensorflow接口进行聚类,使用kmean聚类算法实现。
    注：当前未实现削减无关因素的影响，当前来说，读取注册表内容的API调用非常多，其他的操作相对来说少了很多。
    :return: 
    """
    vectors = input_mtx()
    # 将向量加载到会话中
    tf_vecs = tf.constant(vectors)
    # 当前还不清楚如何取Ｋ值，这里首先就用４
    k = 4
    centroides = tf.Variable(tf.slice(tf.random_shuffle(vectors), [0, 0], [k, -1]))
    expand_vecs = tf.expand_dims(tf_vecs, 0)
    expand_cens = tf.expand_dims(centroides, 1)
    diff = tf.sub(expand_vecs, expand_cens)
    sqr = tf.square(diff)
    distance = tf.reduce_sum(sqr, 2)
    assignments = tf.argmin(distance, 0)

    #计算图心
    means = tf.concat(0, [tf.reduce_mean(tf.gather(vectors, tf.reshape(tf.where(tf.equal(assignments, c)), [1, -1])), reduction_indices=[1])for c in xrange(k)])
    update_centroides = tf.assign(centroides, means)
    init_op = tf.initialize_all_variables()

    # 准备工作就绪 开始
    print "finish initialization... session start..."
    sess = tf.Session()
    sess.run(init_op)
    for step in xrange(100):
        _, centroides_values, assignments_values = sess.run([update_centroides, centroides, assignments])


def main():
    print "tensorflow surport added"
    test_tf()
    # 开始tensorflow训练 
    tf_train()
    return 0


if __name__ == "__main__":
    sys.exit(main())
