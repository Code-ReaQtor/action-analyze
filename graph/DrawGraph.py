#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: DrawGraph.py
@time: 2017/5/8 15:28
"""
import sys
import matplotlib
import math
import random


def draw_log():
    for i in range(1000):
        # 先打0-1之间的点
        x = random.random()
        y = math.log(x)



def main():
    draw_log()
    return 0


if __name__ == '__main__':
    sys.exit(main())

