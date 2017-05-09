#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: find_api.py
@time: 2017/5/9 15:30
"""
import sys


def find_api():
    file_in = open("api_info", 'r')
    content = file_in.readlines()

    for line in content:
        str_array = line.split(' ')
        for word in str_array:
            if 'Nt' in word:
                print word
    file_in.close()


if __name__ == '__main__':
    find_api()

