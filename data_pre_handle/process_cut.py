#!/usr/bin/env python
# encoding: utf-8
"""
@author:luffyren-ubuntu-vm
@date:
@DESC:

"""

import sys
import csv


user_array = []


def add_data_csv(user_name, data):
    """
    将数据添加到对应为csv文件中去
    :param user_name:
    :param data:
    :return:
    """
    if user_name not in user_array:
        user_array.append(user_name)

    file_out = file('../data/after_cut/'+user_name+'.csv', 'ab+')
    file_writer = csv.writer(file_out)
    file_writer.writerow(data)
    file_out.close()


def process_cut(filename):
    """
    将数据文件按某个用户的进程 或者动态库进行划分。分析其进程行为
    :return: 
    """
    """
        :param filename:文件路径
        :return:
        """
    file_in = file(filename, 'rb')
    reader = csv.reader(file_in)

    for line in reader:
        user_name = line[63]
        add_data_csv(user_name=user_name, data=line)

    file_in.close()


def main():
    process_cut("../data/683.csv")

if __name__ == "__main__":
    exit(main())