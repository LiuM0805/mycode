# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/30 14:07
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

print('appium desktop脚本录制')
"""
步骤1：打开appium desktop
步骤2：启动server
步骤3：启动模拟器或真机，adb devices查看设备列表及名称
步骤4：appium1.22版本以后剥离inspector
    方法1：应用程序下载（https://github.com/appium/appium-inspector）
    方法2：网页版（https://inspector.appiumpro.com/）
步骤5：录制脚本（点击搜索框>输入alibaba>点击第一条数据）
总结：定义好设备信息、初始化driver传递给服务、从而达成基本的录制脚本与执行。
"""
# 定义设备信息
desired_cap = {
    "platformName": "Android",  # 指定平台：ios 或 android
    "deviceName": "emulator-5554",  # 获取设备名：adb devices查看
    "appPackage": "com.xueqiu.android",  # 获取包名：adb logcat | grep -i displayed
    "appActivity": ".view.WelcomeActivityAlias",  # 获取页面名：adb logcat | grep -i displayed，重启app
    "noReset": True,  # 是否在测试前后重置环境，例如：登录一次后无需每次都登录
    "dontStopAppOnReset": True,  # 执行完上条用例后不kill应用
    "unicodeKeyBoard": True,  # 结合下面一起使用，支持中文输入
    "resetKeyBoard": True,  # 结合上面一起使用，支持中文输入
}
# 初始化driver，并将设备信息传递给服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

"""下方是desktop录制生成的脚本"""
driver.implicitly_wait(10)  # 添加隐式等待，否则元素找不到
el1 = driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android"
                                ".widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget"
                                ".RecyclerView/android.widget.RelativeLayout["
                                "1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()
driver.quit()
