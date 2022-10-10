# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/9 09:57
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions

print('appium设备交互')


class TestMobile:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.search.USearchActivity",
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        self.driver.make_gsm_call("18888888888", GsmCallActions.CALL)  # 模拟打电话
        self.driver.send_sms("18888888889", "嘿，你在干嘛")  # 模拟发短信
        self.driver.set_network_connection(1)  # 模拟网络连接（无网络、飞行模式、WIFi网络、数据网络、所有网络）
        self.driver.get_screenshot_as_file("./photos/1.png")  # 截图
