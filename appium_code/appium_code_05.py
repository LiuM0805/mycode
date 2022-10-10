# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/7 13:34
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

print('appium显示等待')


class TestWait:
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

    def teardown(self):
        self.driver.quit()

    # 将显示等待可点击，进行封装引用
    def wait_click(self, time, locator):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def test_wait(self):
        print('搜索用例')
        # 显示等待-搜索框可点击
        search_box = (AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        self.wait_click(5, search_box)  # 引用封装好的"显示等待可点击"方法
        self.driver.find_element(*search_box).click()
        # 显示等待-搜索框可输入
        search_send = (AppiumBy.ID, "com.xueqiu.android:id/search_input_text")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(search_send))
        self.driver.find_element(*search_send).send_keys("阿里巴巴")
        # 显示等待-搜索suggest可点击
        search_suggest = (AppiumBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(search_suggest))
        self.driver.find_element(*search_suggest).click()
        # 显示等待-搜索结果页，股票价格可点击
        search_price = (AppiumBy.ID, "com.xueqiu.android:id/current_price")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(search_price))
        el4 = self.driver.find_element(*search_price)
        assert float(el4.text) > 70


if __name__ == '__main__':
    pytest.main()
