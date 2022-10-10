# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/10/5 20:40
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

print('appium触屏操作-滑动')
"""
1.需要导入依赖：from appium.webdriver.common.touch_action import TouchAction
2.常用操作：
    按下：press
    释放：release
    移动：moveto
    点击：tap
    等待：wait
    长按：longPress
    取消：cancel
    执行：perfrom
"""


class TestTouchAction:
    def setup(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": False,
            "dontStopAppOnReset": False,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_slide(self):
        action = TouchAction(self.driver)
        """
        如下方法滑动页面不稳定，不同设备尺寸坐标不准
        action.press(x=711, y=2260).wait(500).move_to(x=711, y=240).release().perform()
        """
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x, y=y_start).wait(500).move_to(x=x, y=y_end).release().perform()


if __name__ == '__main__':
    pytest.main()
