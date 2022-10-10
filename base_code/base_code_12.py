# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/29 12:56
import pytest
import yaml

print('pytest参数化')
"""
语法格式：@pytest.mark.parametrize(参数变量名，参数值)
参数变量名：string(逗号分隔)，list，tuple
参数值：list，list[tuple]
"""


# 使用参数变量名string
@pytest.mark.parametrize("a,b", [(1, 2), (3, 4)])
def test_param01(a, b):
    print(a + b)


# 使用参数变量名list
@pytest.mark.parametrize(["a", "b"], [(5, 6), (7, 8)])
def test_param02(a, b):
    print(a + b)


# 使用参数变量名tuple
@pytest.mark.parametrize(("a", "b"), [(9, 10), (11, 12)])
def test_param03(a, b):
    print(a + b)


print('yaml参数化')
"""
安装第三方yaml模块：pip install pyyaml
加载yaml文件：yaml.safe_load(open("yaml文件路径"))
"""


@pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("base_code_12.yaml")))
def test_param04(a, b):
    print(a + b)
