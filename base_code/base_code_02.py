# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/23 15:07
import random

print('python控制流语法')

"""if条件分支"""
a = 0
print('a=0') if a == 0 else print('a!=0')
"""if多重分支"""
b = 1
print('b=0') if b == 0 else print('b=1') if b == 1 else print('b!=0,1')
"""if嵌套分支（不推荐，推荐使用多重分支）"""
c = 0
if c == 10:
    print('c=优秀')
else:
    if 8 <= c < 10:
        print('c=良好')
    elif 6 <= c < 8:
        print('c=及格')
    elif 1 <= c < 6:
        print('c=不及格')
    else:
        print('c=零分')
"""for循环-计算0-100求和"""
count = 0
for i in range(101):
    count += i
print('0-100求和=%s' % count)
"""for循环-计算0-100偶数求和"""
even_count = 0
for i in range(101):  # 另一种方法：range(2,101,2)
    if i % 2 == 0:
        even_count += i
print('0-100偶数求和=%s' % even_count)
"""while循环"""
a = 0
while a < 3:
    print('a=%s' % a)
    a += 1
else:
    print('a>=3')
"""
break：跳出for、while循环体，并且else块也不执行
continue：跳过当前循环，之后进入下一轮循环
"""
for i in range(1, 11):
    if i == 5:
        break
    print(i)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
"""猜数字游戏-for循环"""
player_input = int(input('请输入0-100之间的数字：'))
random_number = random.randint(0, 100)
for i in range(10):
    if player_input > random_number:
        player_input = int(input('大了，继续：'))
    elif player_input < random_number:
        player_input = int(input('小了，继续：'))
    else:
        print('恭喜你，猜对了')
        break
"""猜数字游戏-while循环"""
while True:
    if player_input > random_number:
        player_input = int(input('大了，继续：'))
    elif player_input < random_number:
        player_input = int(input('小了，继续：'))
    else:
        print('恭喜你，猜对了')
        break
