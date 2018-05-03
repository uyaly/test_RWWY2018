# coding:utf-8
# !/usr/bin/env Python
import unittest
import ddt
import time
from appium import webdriver
from utils.config import Config
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from utils.log1 import Log
import sys
reload(sys)
sys.setdefaultencoding('utf8')
log = Log()

# 休眠15秒等待页面加载完成
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

username = Config().get('ADMIN')
psw = Config().get('PASSWORD')
rodnum = Config().get('RODNUM')
basenum = Config().get('BASENUM')

try:
    # contexts = driver.contexts
    # print contexts
    time.sleep(2)
    # driver.wait_activity(".base.ui.MainActivity", 5)
    # driver.find_element_by_id("username").clear()
    loginpage = driver.find_elements_by_class_name("android.widget.EditText")
    loginpage[0].clear()
    loginpage[0].send_keys(username)
    loginpage[1].clear()
    loginpage[1].send_keys(psw)
    # time.sleep(2)
    # driver.find_element_by_id("btn_submit").click()
    driver.find_element_by_class_name("android.widget.Button").click()
    # driver.find_element_by_accessibility_id("登录").click()
    # driver.find_element_by_android_uiautomator('new UiSelector().description("登录")').click()
    # driver.tap([(45,1074),])
except:
    pass
time.sleep(2)

# 安装工单
menu = driver.find_elements_by_class_name("android.view.View")
menu[5].click()
# 添加杆号
# driver.find_element_by_accessibility_id("杆号管理").click()
# driver.find_element_by_accessibility_id("添加杆号").click()
# driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(rodnum)
# driver.find_element_by_accessibility_id("确定").click()
# # # driver.find_element_by_accessibility_id("杆号列表").click()
# time.sleep(1)
# # 返回
# driver.find_elements_by_class_name("android.view.View")[0].click()
time.sleep(1)
# 添加基站
driver.find_element_by_accessibility_id("基站管理").click()
driver.find_element_by_accessibility_id("添加基站").click()
time.sleep(1)
# 添加手机图片
# driver.find_element_by_accessibility_id("add_picture").click()
# driver.tap([(366,1812),])
# driver.find_element_by_name("相册").click()
# driver.find_element_by_id("com.miui.gallery:id/pick_num_indicator").click()
# driver.find_elements_by_class_name("android.widget.TextView")[1].click()

# 输入基站物理编号
driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(basenum)
# 输入杆号
driver.find_elements_by_class_name("android.widget.EditText")[2].send_keys(rodnum)
driver.find_element_by_accessibility_id("查询杆号").click()
time.sleep(1)
driver.tap([(366,1812),])
# 软件版本
driver.find_elements_by_class_name("android.widget.EditText")[5].send_keys("1.0")
# 联系人
driver.find_elements_by_class_name("android.widget.EditText")[6].send_keys(u"张三")
driver.swipe(100, 100, 100, 1000)
# print len(ll)
# for i in range(len(ll)):
#     if i >4:
#         print(i)
#         ll[i].click()
# driver.find_element_by_accessibility_id("install").click()
# driver.find_element_by_android_uiautomator('new UiSelector().description("安装工单")').click()

# driver.quit()