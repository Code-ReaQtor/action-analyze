#/usr/bin/python
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:

"""
import tensorflow as tf
import sys


def test_tf():
    a = tf.placeholder("float")
    b = tf.placeholder("float")
    y = tf.multiply(a, b)
    sess = tf.Session()
    print sess.run(y, feed_dict={a: 3, b: 3})



def main():
    print "tensorflow surport added"
    test_tf()
    return 0


if __name__ == "__main__":
    sys.exit(main())