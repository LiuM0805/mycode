# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/29 13:26
import pytest
import yaml

print('python数据驱动')
"""
数据驱动简介：数据改变从而驱动自动化测试执行，最终引起测试结果改变。
应用场景：测试步骤、测试数据、配置数据，三种数据驱动。
"""


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./base_code_13.yaml")))
    def test_demo(self, env):
        if 'test' in env:
            print('这是测试环境')
            print(env['test'])
        elif 'dev' in env:
            print('这是开发环境')
            print(env['dev'])
