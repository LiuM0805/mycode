# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/10 09:14
print('找出最长公共前缀')

"""找出最长公共前缀"""
a = ["flower", "flow", "flight"]
result = ''
for i in zip(*a):
    set_content = set(i)
    if len(set(i)) == 1:
        result += i[0]
    else:
        break
print(result)
