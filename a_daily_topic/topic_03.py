# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/10 09:16
print('九九乘法表')

"""九九乘法表"""
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f'{y}*{x}={x * y}', end=' ')
    print('')
