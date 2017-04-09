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
    mtx_file.close()
    vectors = []
    return vectors


def tf_train():
    """
    使用tensorflow接口进行聚类
    :return: 
    """
    vectors = input_mtx()
    tf_vecs = tf.constant(vectors)
    # 当前还不清楚如何取Ｋ值，这里首先就用４
    k=4
    



def main():
    print "tensorflow surport added"
    test_tf()
    return 0


if __name__ == "__main__":
    sys.exit(main())
