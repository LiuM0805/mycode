# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/26 20:59
import math
import os
import time
import urllib.request

print('python标准库')

"""os模块，主要针对文件、目录操作"""
# os.mkdir('tmp')  # 创建目录
# os.removedirs('tmp')  # 删除目录
print(os.getcwd())  # 获取当前目录
print(os.listdir())  # 获取当前目录和文件
print(os.path.exists('base_code_08.py'))  # 判断文件或目录是否存在

"""time模块，主要针对时间操作"""
print(time.asctime())  # 国外的时间格式
print(time.time())  # 时间戳
time.sleep(1)  # 等待时间
print(time.localtime())  # 时间戳转成元祖
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 将元祖类型时间格式转成带格式的时间
# 获取两天前的时间
two_day = time.time() - 60 * 60 * 24 * 2  # 步骤1：当前时间戳 减 2天所消耗的秒数
time_tuple = time.localtime(two_day)  # 步骤2：将2天前的时间戳转成元祖
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))  # 步骤3：传入元祖时间格式转成带格式的时间

"""urllib模块，主要针对网络请求"""
response = urllib.request.urlopen('http://www.baidu.com')  # 第三方库requests基于urllib.request进行二次封装的。
print(response.status)

"""math模块，主要针对科学计数"""
print(math.ceil(5.5))  # 大于5.5最大整数
print(math.floor(5.5))  # 小于5.5最大整数
