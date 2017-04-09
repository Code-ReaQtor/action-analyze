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
    :return: 
    """
    mtx_file = open("vector.json", 'r')
    pass


def tf_train():
    """
    使用tensorflow接口进行聚类
    :return: 
    """
    pass


def main():
    print "tensorflow surport added"
    test_tf()
    return 0


if __name__ == "__main__":
    sys.exit(main())
