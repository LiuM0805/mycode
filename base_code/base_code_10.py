# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/28 16:13
import time
import unittest

print('unittest框架')

"""
导入unittest模块：import unittest
类定义：class TestDemo(unittest.TestCase) 
用例方法命名：test_*
setUp和teardown，方法前后分别调用
setUpClass和teardownClass，类前后分别调用
"""


class TestDemo01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setup class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test_01(self):
        time.sleep(1)
        print('测试用例01')


class TestDemo02(unittest.TestCase):
    def test_02(self):
        time.sleep(1)
        print('测试用例02')


"""用例执行方法"""
if __name__ == '__main__':
    # 方法一：执行当前所有unittest测试用例
    unittest.main()
    # 方法二：利用套件，执行指定测试用例
    suite = unittest.TestSuite()
    suite.addTest(TestDemo01("test_01"))
    unittest.TextTestRunner().run(suite)
    # 方法三：执行指定测试类
    suite_class_01 = unittest.TestLoader().loadTestsFromTestCase(TestDemo01)
    suite_class_02 = unittest.TestLoader().loadTestsFromTestCase(TestDemo02)
    suite = unittest.TestSuite([suite_class_01, suite_class_02])
    unittest.TextTestRunner().run(suite)
    # 方法四：匹配某个目录下所有用例
    test_dir = r'/base_code/'
    suite_discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    unittest.TextTestRunner().run(suite_discover)
