# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/30 13:58
print('题目：列表中两个数字相加等于目标值，打印下标')

"""列表中两个数字相加等于目标值，并打印下标"""
nums = [2, 7, 11, 15]
target = 18
for x in range(len(nums)):
    for y in range(x + 1, len(nums)):
        if target - (nums[x] + nums[y]) == 0:
            print([x, y])
