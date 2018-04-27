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
                'appPackage': 'com.ycig.app.ilink',
                # apk的launcherActivity
                'appActivity': 'com.ycig.app.ilink.MainActivity',
                # unicodeKeyboard是使用unicode编码方式发送字符串
                'unicodeKeyboard': True,
                # resetKeyboard是将键盘隐藏起来
                'resetKeyboard': True
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 休眠15秒等待页面加载完成
time.sleep(5)
Number = Config().get('PLATENUMBER')
chipId = Config().get('CHIPID')
# driver.find_element_by_id("username").send_keys("18062427385")
# driver.find_element_by_id("password").send_keys("000000")
# 点击地图上的电动车头像
driver.find_element_by_accessibility_id(Number).click()
# 设防
driver.find_element_by_accessibility_id("设防").click()
# 撤防
driver.find_element_by_accessibility_id("撤防").click()
# 一键报警
driver.find_element_by_accessibility_id("报警").click()
# 报警记录
driver.find_element_by_accessibility_id("报警记录").click()
# 历史轨迹
driver.find_element_by_accessibility_id("历史轨迹").click()


# 进目录
# driver.quit()