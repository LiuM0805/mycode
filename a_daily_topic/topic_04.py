# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/10 09:16
print('找出回文数')

"""找出回文数"""
num = 123
list_num = list(str(num))
if list_num[0:] == list_num[::-1]:
    print(True)
else:
    print(False)
