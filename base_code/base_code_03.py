# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/23 19:49

print('python函数')
"""
函数，以def开头接函数名称接圆括号，例如：def func()
函数，圆括号中定义参数，例如：def func(val)
函数，内部输入三个双引号，可生成该函数说明文档
return[表达式]，结束函数并选择性返回一个值给调用方，不加return或return不带函数均返回None
"""


# 函数定义
def func_01():
    print('这是一个函数')


# 函数调用
func_01()


# 参数定义
def func_02(a, b, c):
    # pycharm快捷键：command+d自动复制上一行代码
    print('这是一个参数a，值：', a)
    print('这是一个参数b，值：', b)
    print('这是一个参数c，值：', c)


# 函数调用并使用位置传参，这个方式参数与定义位置要对应上
func_02(1, 2, 3)
# 函数调用并使用关键字参数，这个方式可以随便变更位置
func_02(b=2, a=1, c=3)
# 函数调用并使用混合传参，这个方式位置参数在前关键字参数在后
func_02(1, c=3, b=2)


# return函数表达式
def func_03(a, b, c):
    return f'这是一个return，表达式是a+b+c，值：{a + b + c}'


# 打印return返回值
print(func_03(1, 2, 3))


# 默认参数定义
def func_04(a=1):
    print('这是一个默认参数a，值：', a)


# 函数调用并使用默认参数
func_04()

"""
lambda表达式，主体是表达式，不是代码块，仅封装有限逻辑
"""
func_lambda = lambda x: x * 2
print('这是一个lambda表达式：', func_lambda(2))
