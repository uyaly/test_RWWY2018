# coding:utf-8
# !/usr/bin/env Python
import unittest
import ddt
from appium import webdriver
from utils.config import Config
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from utils.log1 import Log

log = Log()

# 休眠15秒等待页面加载完成
@ddt.ddt
class setup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        desired_caps = {
                    # 这里是声明android还是ios的环境
                    'platformName': 'Android',
                    # 手机设备名称，通过adb devices查看
                    'deviceName': '11642f40',
                    # android系统的版本号
                    'platformVersion': '6.0.1',
                    # apk包名
                    'appPackage': 'com.ycig.app.facility',
                    # apk的launcherActivity
                    'appActivity': 'com.ycig.app.facility.MainActivity',
                    # unicodeKeyboard是使用unicode编码方式发送字符串
                    'unicodeKeyboard': True,
                    # resetKeyboard是将键盘隐藏起来
                    'resetKeyboard': True
                    }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def test01_login(self):
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.find_element_by_id("username").send_keys(self.username)
        self.find_element_by_id("password").send_keys(self.psw)
        # 进目录
        self.quit()