# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/3 16:36
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

print('appium元素定位')
"""
1.打开雪球app
2.点击搜索框
3.输入中文阿里巴巴
4.搜索结果页，点击阿里巴巴
5.获取阿里巴巴股价
6.断言股价大于70
"""


class TestLocation:
    def setup(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print('搜索用例')
        # id定位
        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        # xpath定位
        el3 = self.driver.find_element(
            by=AppiumBy.XPATH,
            value='//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/current_price")
        assert float(el4.text) > 70


if __name__ == '__main__':
    pytest.main()
