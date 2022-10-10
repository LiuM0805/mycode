# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/8 19:42
import time
from appium import webdriver

print('android webview测试')
"""
设备准备：
1. 查看浏览器包名：adb shell pm list | grep browser
2. 查看浏览器版本信息：adb shell pm dump 包名 | grep version
驱动准备：
1. 应用程序Appium Server GUI，右键点击显示包内容
2. 进入路径：/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac
    注意：appium默认在该目录查找driver，声明driver环境变量的请忽略此目录
3. 将selenium的chromedriver复制到该路径下
代码变更：
1. caps设备信息：appPackage、appActivity替换成："browserName": "Browser"
2. 指定chromedriver："chromedriverExecutable": "路径"
"""


class TestWebView:
    def setup(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "browserName": "Browser",
            "noReset": True,
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.get('http://m.baidu.com')
        time.sleep(5)
