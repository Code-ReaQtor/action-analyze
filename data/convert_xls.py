#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: convert_xls.py
@time: 2017/5/10 16:30
"""
import xlwt
import json
import random

software = {
    "QQ":   [
        'NtQueryValueKey',
        'NtCreateUserProcess',
        'Recv',
        'RecvFrom',
        'Send',
        'SendTo',
      ],
    "explorer": [
        'NtQueryValueKey',
        'Recv',
        'NtReadCookies',
        'NtOpenProcess',
        'NtCreateUserProcess',
    ],

    "edit_tool": [
        'NtQueryValueKey',
        'NtWriteFile',
        'NtCreateUserProcess'
    ],
    
    "spy": [
        'NtQueryValueKey',
        'RegEnumKey',
        'NtOpenFile',
        'NtReadFile'
    ],

    "soldier": [
        'NtQueryValueKey',
        'NtOpenFile',
        'NtReadFile',
    ]
}


def write_xls():
    """
    读取各类程序的特点字典，生成excel表格方便制图。
    :return:
    """
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    api_file = open('windows_api.json', 'r')
    api_map = json.load(api_file)

    for (cluster, keyword) in software.items():
        sheet = book.add_sheet(cluster, cell_overwrite_ok=True)
        idx = 0
        for (k, v) in api_map.items():
            sheet.write(0, idx, k)
            if k not in keyword:
                sheet.write(1, idx, little_random())
            else:
                sheet.write(1, idx, big_random())
            idx += 1
    book.save(r'api_map.xls')
    api_file.close()


def little_random():
    """
    产生0-10之间的随机数
    :return:
    """
    return random.randint(0, 30)


def big_random():
    """
    产生50-100之间的随机数
    :return:
    """
    return random.randint(50, 100)

if __name__ == '__main__':
    write_xls()

