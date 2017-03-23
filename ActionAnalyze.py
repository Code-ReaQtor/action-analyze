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
        op, args = getopt.getopt(sys.argv[1:],"hp:i:",["help", "port=", "ip="])
        for op_name, op_value in op:
            if op_name in("--help","-h"):
                show_how_to_use()

    except getopt.GetoptError:
        print "argument error system exit..."
        sys.exit(-1)


if __name__ == '__main__':
    sys.exit(main())

