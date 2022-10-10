# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/26 16:05
print('python错误与异常')
"""
错误与异常的区别：异常可以被捕获和处理；错误一般多见于：编码错误、逻辑错误、系统错误
"""

"""异常处理"""
list_a = [1, 2, 3]
try:
    print(list_a[3])
except Exception as e:
    print('有异常，走我')
    print(e)
else:
    print('没有异常，走我')
finally:
    print('有没有异常，都走我')

"""主动抛异常"""
a = 0
if a == 0:
    raise ValueError(f'值错误，值是：{a}')
else:
    print(f'a={a}')

'''主动抛异常 和 自定义异常使用时，记得先注释一种-----------'''


# 自定义异常
class MyException(Exception):
    def __init__(self, msg):
        print(f'这是自定义异常：{msg}')


# 引用自定义异常
if a == 0:
    raise MyException(f'值错误，值是：{a}')
else:
    print(f'a={a}')
