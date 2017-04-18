#/usr/bin/python
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:

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
    mtx_file = open("vector.json", 'r')
    #　加载向量
    vec_dict = json.load(mtx_file)
    vectors = []
    for value in vec_dict:
        vectors.append(value)
    mtx_file.close()
    return vectors


def tf_train():
    """
    使用tensorflow接口进行聚类,使用kmean聚类算法实现
    :return: 
    """
    vectors = input_mtx()
    # 将向量加载到会话中
    tf_vecs = tf.constant(vectors)
    # 当前还不清楚如何取Ｋ值，这里首先就用４
    k=4
    centroides = tf.Variable(tf.slice(tf.random_shuffle(vectors)))
    expand_vecs = tf.expand_dims(tf_vecs, 0)
    expand_cens = tf.expand_dims(centroides, 1)
    diff = tf.sub(expand_vecs, expand_cens)
    sqr = tf.square(diff)
    

    #计算图心
    means = tf.concat(0, [tf.reduce_mean(tf.gather(vectors,tf.reshape(tf.where(tf.equal(assignments,c)),[1,-1])),reduction_indices=[1])forcinxrange(k)])

    init_op = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init_op)





def main():
    print "tensorflow surport added"
    test_tf()
    return 0


if __name__ == "__main__":
    sys.exit(main())
