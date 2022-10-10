# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/23 20:42

print('python数据结构')
"""
Python的六大数据类型：数字(Number) 字符串(String) 元组(Tuple) 列表(List) 集合(Set) 字典(Dictionary)
Python的可变类型：列表、集合、字典(可以进行更改,并且更改后物理地址不会发生改变)
Python的不可变类型：数字、字符串、元组(不可以进行更改,更改后就是一个新的对象了,物理地址发生了变化)
"""

"""列表"""
list_a = [3, 1, 2]  # 定义列表
list_a.append(4)  # 末尾追加数据
list_a.insert(0, 9)  # 指定索引位置插入数据
list_a.remove(4)  # 移除指定的值
list_a.pop(0)  # 指定索引位置删除数据，并返回该值
list_a.sort()  # 升序排序
list_a.sort(reverse=True)  # 降序排序
list_a.reverse()  # 反转输出
list_a.count(1)  # 统计指定值的出现次数
list_a.index(2)  # 输出参数的索引值
print(list_a)
list_equation = [i for i in range(4) if i != 0]  # 列表推导式
print('列表推导式：', list_equation)
"""元祖"""
tuple_a = (1, 2, 3)  # 定义元祖
tuple_b = 1, 2, 3  # 定义元祖
# 元组里索引3的位置列表是可变的，因为列表内是可变的，但要将列表改为字符则不可变
tuple_c = (1, 2, 3, [4, 5, 6])
tuple_c[3][0] = 'a'
print('元祖不可变类型特性：', tuple_c)
"""集合"""
set_a = {1}  # 定义集合，该方法数据不可为空，为空就是字典类型了
set_b = set('1')  # 定义集合，该方法数据可为空
set_c = {1, 2, 3}
set_d = {1, 4, 5}
print('并集', set_c.union(set_d))  # 打印set_c和set_d并集
print('交集', set_c.intersection(set_d))  # 打印set_c和set_d交集
print('差集', set_c.difference(set_d))  # 打印set_c和set_d差集
set_e = {1}
set_e.add(2)
print('集合添加参数：', set_e)  # 添加参数
"""字典"""
dict_a = {"a": 1, "b": 2}  # 定义字典
dict_b = dict(a=1, b=2)  # 定义字典
print('dict_a：%s；dict_b：%s' % (dict_a, dict_b))
dict_a.keys()  # 获取所有key
dict_a.values()  # 获取所有value
