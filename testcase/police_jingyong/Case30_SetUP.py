# coding:utf-8
# !/usr/bin/env Python
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from utils.config import Config
from utils.log1 import Log

desired_caps = {
                # 这里是声明android还是ios的环境
                'platformName': 'Android',
                # 手机设备名称，通过adb devices查看
                'deviceName': '11642f40',
                # android系统的版本号
                'platformVersion': '6.0.1',
                # apk包名
                'appPackage': 'com.cordova.policeapp',
                # apk的launcherActivity
                'appActivity': 'com.cordova.policeapp.MainActivity',
                # unicodeKeyboard是使用unicode编码方式发送字符串
                'unicodeKeyboard': True,
                # resetKeyboard是将键盘隐藏起来
                'resetKeyboard': True
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 休眠15秒等待页面加载完成
time.sleep(5)
chipId = Config().get('CHIPID')
# driver.find_element_by_id("username").send_keys("18062427385")
# driver.find_element_by_id("password").send_keys("000000")
driver.find_element_by_accessibility_id("报警记录").click()
# 搜索
driver.find_element_by_accessibility_id("headRightString").click()
driver.find_element_by_class_name("android.widget.EditText").send_keys(chipId)
driver.find_element_by_accessibility_id("搜索").click()
# 需要修改bug后才能看到按钮

# 进目录

# driver.quit()