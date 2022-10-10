# !/usr/bin/env python
# -*- coding: utf-8 -*-
# liumiao 2022/9/29 14:04
import allure

print('Allure报告框架')
"""
安装第三方Allure服务
安装第三方allure-pytest模块：pip install allure-pytest
运行用例：pytest [测试文件] -v -s -q --alluredir="存储报告路径" --clean-alluredir(清理残留case)
查看报告方法1：allure serve [存储的报告路径]
查看报告方法2：
    allure generate [报告路径] -o [指定生成报告路径] -c
    allure open -h 127.0.0.1 -p 8083 [合成后的报告路径]
allure标注模块、功能、方法名、测试步骤、链接：
    标注功能：@allure.feature("功能名称")
    标注子功能：@allure.story("子功能名称")
    标注测试步骤：@allure.step("测试步骤")
    标注链接：@allure.testcase("url", "链接名称")
    执行feature用例：pytest base_code_14.py --allure-features="模块名" -v -s
    执行story用例：pytest base_code_14.py --allure-stories="模块名" -v -s
    feature与story类似父子关系
allure标注测试用例级别：
    标注用例级别：@allure.severity(allure.severity_level.级别)
    级别分类：
        blocker 阻塞缺陷（功能未实现，无法下一步）
        critical严重缺陷（功能点缺失）
        normal 一般缺陷（边界情况，格式错误）
        minor 次要缺陷（界面错误与ui需求不符）
        trivial 轻微缺陷（必须项无提示，或者提示不规范）
allure添加文本、html代码块、图片、视频
    添加文本：allure.attach("这是文本",name="文本名称", attachment_type=allure.attachment_type.TEXT)
    添加html：allure.attach("<body>代码块</body>", name="代码块名称", attachment_type=allure.attachment_type.HTML)
    添加图片：allure.attach.file('图片路径', name='图片名称', attachment_type=allure.attachment_type.图片格式)
    添加视频：allure.attach.file('视频路径', name='视频名称', attachment_type=allure.attachment_type.视频格式)
"""


@allure.feature('模块名称')
class TestLogin:
    @allure.story('用例名称')
    @allure.step('装饰器形式使用step')
    @allure.title('登录成功')
    def test_login_success(self):
        with allure.step('包含在语句里使用step，步骤1：输入用户名'):
            print('输入用户名')
        with allure.step('包含在语句里使用step，步骤2：输入密码'):
            print('输入密码')
        print('登录成功')

    @allure.testcase('http://www.baidu.com', 'allure添加链接的名称')
    def test_link(self):
        print('allure链接添加')

    @allure.severity(allure.severity_level.MINOR)
    def test_level(self):
        print('allure设置用例级别')

    def test_add_text(self):
        print('报告中添加文本')
        allure.attach('文本内容', name='文本名称', attachment_type=allure.attachment_type.TEXT)

    def test_add_html(self):
        print('报告中添加html')
        # 如果代码块包含单双引号，外侧使用三个单双引号例如："""代码块"""
        allure.attach("<body>代码块</body>", name="代码块名称", attachment_type=allure.attachment_type.HTML)

    def test_add_photo(self):
        print('报告中添加图片')
        allure.attach.file('/Users/liumiao/PycharmProjects/mycode/base_code/base_code_14.JPG', name='图片名称',
                           attachment_type=allure.attachment_type.JPG)

    def test_add_video(self):
        print('报告中添加视频')
        allure.attach.file('/Users/liumiao/PycharmProjects/mycode/base_code/base_code_14.mp4', name='视频名称',
                           attachment_type=allure.attachment_type.MP4)
