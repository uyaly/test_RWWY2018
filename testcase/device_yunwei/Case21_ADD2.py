# coding:utf-8
# !/usr/bin/env Python
import unittest
import ddt
import time
from appium import webdriver
from utils.config import Config
from utils.config import XlsData
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
            'deviceName': 'cc2ae2f4',   # 公司 cc2ae2f4，自己 11642f40
            # android系统的版本号
            'platformVersion': '6.0.1',
            # apk包名
            'appPackage': 'com.ycig.app.facility',
            # apk的launcherActivity
            'appActivity': 'com.ycig.app.facility.MainActivity',
            # unicodeKeyboard是使用unicode编码方式发送字符串
            # 'unicodeKeyboard': True,
            # # resetKeyboard是将键盘隐藏起来
            # 'resetKeyboard': True
            }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

username = Config().get('ADMIN')
psw = Config().get('PASSWORD')
rodnum = XlsData()
basenum = Config().get('BASENUM')
# rodnum = XlsData().get('RODNUM')
# basenum = XlsData().get('BASENUM')
# 登录
try:
    time.sleep(2)
    # driver.wait_activity(".base.ui.MainActivity", 5)
    # driver.find_element_by_id("username").clear()
    loginpage = driver.find_elements_by_class_name("android.widget.EditText")
    loginpage[0].clear()
    loginpage[0].send_keys(username)
    loginpage[1].clear()
    loginpage[1].send_keys(psw)
    driver.find_element_by_class_name("android.widget.Button").click()
except:
    pass
time.sleep(2)

# 安装工单
driver.find_elements_by_class_name("android.view.View")[5].click()
# 添加杆号
driver.find_element_by_accessibility_id("杆号管理").click()
driver.find_element_by_accessibility_id("添加杆号").click()
time.sleep(1)
for i in range(len(rodnum)):
    driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(rodnum[i])  # 输入杆号
    driver.find_element_by_accessibility_id("添加下一个").click()

time.sleep(2)
# 返回
driver.find_elements_by_class_name("android.view.View")[1].click()
time.sleep(2)
# 添加基站
driver.find_element_by_accessibility_id("基站管理").click()
driver.find_element_by_accessibility_id("添加基站").click()
time.sleep(2)
# 添加手机图片
driver.find_element_by_accessibility_id("add_picture").click()
time.sleep(1)
driver.tap([(366,1812),])
time.sleep(2)
driver.find_element_by_name("相册").click()
driver.find_elements_by_id("com.miui.gallery:id/pick_num_indicator")[1].click()  # 选第二张图
# 输入信息
driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys(basenum)  # 输入基站物理编号
driver.find_elements_by_class_name("android.widget.EditText")[2].send_keys(rodnum)  # 输入杆号
driver.find_element_by_accessibility_id("查询杆号").click()
time.sleep(1)
driver.tap([(366,1812),])
time.sleep(2)
driver.swipe(100, 1000, 100, 50,0)  # 滑动
driver.find_elements_by_class_name("android.widget.EditText")[5].send_keys("v 1.0")  # 软件版本
driver.find_element_by_accessibility_id("添加下一个").click()
time.sleep(5)
# 判断
try:
    assert driver.find_elements_by_class_name("android.view.View")[4].get_attribute("name") == basenum, "新增基站未找到"
    print("新增基站成功")
except AssertionError,msg:
    print msg

# ll = driver.find_elements_by_class_name("android.view.View")
# ll = driver.find_element_by_name("")
# print len(ll)
# for i in range(len(ll)):
#     print str(i) + ":" + ll[i].get_attribute("name")
        # ll[i].click()


driver.quit()