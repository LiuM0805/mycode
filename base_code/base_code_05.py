# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/26 10:18
import json

print('python输入与输出')
"""
字面量插值：将变量、常量及表达式之间进行插入技术，避免很多字符串拼接问题。
"""

"""字面量插值"""
str_name = 'abc'
int_num = 5
print('%%s输出字符：%s，%%d输出数字：%d' % (str_name, int_num))  # 格式化输出优势：%.2f可控制小数点位数
list_a = [1, 2, 3]
dict_a = {'a': 1, 'b': 2, 'c': 3}
print('format输出列表：{}，format输出字典：{}'.format(list_a, dict_a))
print('format输出下标位置对应数据：{1}{0}'.format(list_a, dict_a))
print('format输出解包列表值：下标0={}，下标1={}'.format(*list_a))
print('format输出解包字典值：key值a={a}，key值b={b}'.format(**dict_a))  # format()输出优势：可控制输出数据
print(f'f-string输出列表下标0的值：{list_a[0]}')  # f{string}输出优势：可输出变量、常量、表达式等
"""Json使用方式"""
# JSON由字典和列表组成
j = {
    "name": ['jerry', 'james'],
    "age": 30
}
dict_str = json.dumps(j)  # 将数据类型转成字符串
print(dict_str)
str_json = json.loads(dict_str)  # 将字符串转成json
print(str_json)
