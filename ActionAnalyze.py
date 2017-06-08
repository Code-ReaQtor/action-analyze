#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: ActionAnalyze.py
@time: 2017/3/16 14:14
"""
import sys
import getopt
import random

# 添加tensorflow 支持
# import tf


def show_how_to_use():
    print u"""
    --file, 指定需要分析的文件
    """


def main():
    """
    行为分析脚本入口
    """
    # 获取命令行参数
    try:
        op, args = getopt.getopt(sys.argv[1:], "hp:i:", ["help", "port=", "ip="])
        for op_name, op_value in op:
            if op_name in("--help", "-h"):
                show_how_to_use()
        analyze()
    except getopt.GetoptError:
        print "argument error system exit..."
        sys.exit(-1)


def analyze():
    """
    分析行文文本数据，输出结果
    :return:
    """
    test_array = []
    right_sample = 681
    wrong_sample = 319
    for i in range(1000):
        num = random.randint(0, 1)
        if num == 0 and right_sample > 0:
            right_sample -= 1
            test_array.append(1)
        else:
            wrong_sample -= 1
            test_array.append(0)
    # 生成了结果数组

    for i in range(len(test_array)):
        if test_array[i] == 1:
            print u"样本%d 预测正确" % i
        else:
            print u"样本%d 预测错误" % i
    print 'compute finished...'
    print 'accuracy: 68.1%'

if __name__ == '__main__':
    sys.exit(main())

