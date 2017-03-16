#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: data_cut.py
@time: 2017/3/13 14:54
"""
import os
import json
import csv

api_map = {}
user_array = []


def add_data(user_name, data):
    """
    将数据添加到对应的文件中去，name => name.txt
    :param user_name:
    :param data:
    :return:
    """
    if user_name not in user_array:
        user_array.append(user_name)

    file_out = open(user_name + '.txt', 'a')
    file_out.write(data)
    file_out.close()


def add_data_csv(user_name, data):
    """
    将数据添加到对应为csv文件中去
    :param user_name:
    :param data:
    :return:
    """
    if user_name not in user_array:
        user_array.append(user_name)

    file_out = file(user_name, 'wb')
    file_writer = csv.writer(file_out)
    file_writer.writerow(data)


def cut(filename):
    """
    读取数据文件，按照用户名切分为多个用户的行为数据
    :param filename:
    :return:
    """
    file_in = open(filename, 'r')

    while True:
        line = file_in.readline()
        row = line.split(',')
        user_name = row[2]
        add_data(user_name=user_name, data=line)

        api_name = row[3]
        if api_name not in api_map:
            api_map[api_name] = row[4]

        if 0:
            break       #当读取到文件尾的时候跳出循环

    file_in.close()


def cut_csv(filename):
    """

    :param filename:
    :return:
    """
    file_in = file(filename, 'rb')
    reader = csv.reader(file_in)

    for line in reader:
        line = file_in.readline()
        user_name = line[3]
        add_data_csv(user_name=user_name, data=line)

        api_name = line[28]
        if api_name not in api_map:
            api_map[api_name] = line[49]

    file_in.close()


def print_csv(filename):
    """

    :param filename:
    :return:
    """
    file_in = file(filename, 'rb')
    reader = csv.reader(file_in)

    flag = True
    for line in reader:
        if not flag:
            flag = True
            continue
        print line
        print type(line)
        for i in range(0, len(line)-1):
            print "%d : %s" % (i, line[i])
        break

    file_in.close()


def generate_api_map():
    """
    生成API 编号表
    :return:
    """
    file_out = open('../data/api_map.txt', 'w')
    # 将得到的dist 按照 value 值进行排序 得到一个固定的顺序
    api_map_data = json.dumps(api_map)
    file_out.write(api_map_data)
    file_out.close()

if __name__ == '__main__':
    """
    切分数据文件脚本入口
    """
    computer_action_data = "../data/683.csv"
    # cut(computer_action_data)
    # generate_api_map()
    #print_csv(computer_action_data)
    cut_csv(computer_action_data)

