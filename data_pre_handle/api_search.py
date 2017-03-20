#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: api_search.py
@time: 2017/3/17 15:35
"""

import json
import csv
import sys


def generate_api_map(filename):
    """
    生成API 编号表
    :return:
    """
    csv.field_size_limit(sys.maxsize)
    
    api_map = {}
    file_in = file(filename, 'rb')
    reader = csv.reader(file_in)
    try:
        for line in reader:
            api_map[line[28]] = line[49]
    except csv.Error:
        print "文件长度超过限制。系统不好解决。"

    file_out = open('../data/api_map.json', 'w')
    # 将得到的dist 按照 value 值进行排序 得到一个固定的顺序
    api_map_data = json.dumps(api_map)
    file_out.write(api_map_data)

    file_in.close()
    file_out.close()


if __name__ == '__main__':
    generate_api_map(filename="../data/683.csv")

