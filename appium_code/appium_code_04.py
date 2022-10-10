# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/5 21:20
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

print('appium触屏操作-解锁demo')


class TestUnlock:
    def setup(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.android.settings",  # 解锁包名
            "appActivity": ".ConfirmLockPattern$InternalActivity",  # 解锁页面
            "noReset": False,
            "dontStopAppOnReset": False,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        action.press(x=435, y=931).wait(1000).move_to(x=701, y=931).wait(1000).move_to(x=971, y=931).wait(1000) \
            .move_to(x=971, y=1205).wait(1000).move_to(x=971, y=1466).release().perform()


if __name__ == '__main__':
    pytest.main()
