# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/7 14:32
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

print('appium识别toast')


class TestToast:
    def setup(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.search.USearchActivity",
            "noReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        print('添加股票')
        # 搜索框输入
        self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 点击suggest
        search_suggest = (AppiumBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
        self.driver.find_element(*search_suggest).click()
        # 点击加自选
        add = (AppiumBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/follow_btn" and @text="加自选"]')
        self.driver.find_element(*add).click()
        # 断言toast==添加成功
        get_toast = self.driver.find_element(AppiumBy.XPATH, '//*[@class="android.widget.Toast"]')
        assert get_toast.text == '添加成功'
        # 点击取消添加
        cancel_add = (AppiumBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/followed_btn" and @text="已添加"]')
        self.driver.find_element(*cancel_add).click()
        # 断言toast==已从自选删除
        get_toast = self.driver.find_element(AppiumBy.XPATH, '//*[@class="android.widget.Toast"]')
        assert get_toast.text == '已从自选删除'


if __name__ == '__main__':
    pytest.main()
