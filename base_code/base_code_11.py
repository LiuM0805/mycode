# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/28 21:28
import pytest

print('pytest框架')


def func(x):
    return x + 1


# 装饰器使用
@pytest.fixture()
def login():
    username = 'aaa'
    return username


class TestDemo:
    # 参数化使用
    @pytest.mark.parametrize('a,b', [
        (1, 2),
        (10, 20)
    ])
    def test_answer(self, a, b):
        assert func(a) == b

    def test_01(self, login):
        print(f'测试用例01需要登录，用户名：{login}')

    def test_02(self):
        print('测试用例02不需要登录')


if __name__ == '__main__':
    pytest.main(['base_code_11.py'])
