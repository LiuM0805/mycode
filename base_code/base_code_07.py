# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/26 19:49
print('python面向对象编程')


# 通过class关键字，定义一个(人)类
class Person:
    # 类变量
    name = 'liu'
    age = 30

    # 初始化方法__init__，在下面你实例化时同时执行
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_param(self, name):
        # self.变量名：实例变量
        self.name = name

    @classmethod
    def play_basketball(self):
        print('playing basketball')


"""实例化"""
zs = Person('张三', 18)  # 实例化zs
zs.play_basketball()  # 实例化play_basketball方法
# zs.set_param('zhangsan')  # 实例化set_param方法并传参
print(f'姓名：{zs.name}；年龄：{zs.age}')

"""类变量 和 实例变量区别"""
print(Person.name)  # 类变量调用时需要类来访问，但是只能访问自己默认的一些属性值
example = Person('李四', 18)
print(example.name)  # 实例变量需实例来访问，所以要先进行实例化example并设定属于自己的属性值

"""类方法 和 实例方法区别"""
# 提示缺少self，因为self代表实例，类不可以调用实例方法
# 如果类方法想调用成功，需要给该方法加装饰器@classmethod
Person.play_basketball()
# 实例化ww可以调用，因为ww实例化时默认把自身self实例带入进去
ww = Person('王五', 18)
ww.play_basketball()
