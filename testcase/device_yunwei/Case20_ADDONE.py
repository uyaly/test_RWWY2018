# coding:utf-8
# !/usr/bin/env Python
import unittest
import ddt
import time
from appium import webdriver
from utils.config import Config
import sys
reload(sys)
sys.setdefaultencoding('utf8')

@ddt.ddt
class setup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        desired_caps = {
                    # 这里是声明android还是ios的环境
                    'platformname': 'android',
                    # 手机设备名称，通过adb devices查看
                    'devicename': '11642f40',
                    # android系统的版本号
                    'platformversion': '6.0.1',
                    # apk包名
                    'apppackage': 'com.ycig.app.facility',
                    # apk的launcheractivity
                    'appactivity': 'com.ycig.app.facility.mainactivity',
                    # unicodekeyboard是使用unicode编码方式发送字符串
                    'unicodekeyboard': True,
                    # resetkeyboard是将键盘隐藏起来
                    'resetkeyboard': True
                    }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test01_login(self):
        # 登录
        try:
            time.sleep(2)
            self.username = Config().get('admin')
            self.psw = Config().get('password')
            loginpage = self.driver.find_elements_by_class_name("android.widget.edittext")
            loginpage[0].clear()
            loginpage[0].send_keys(self.username)
            loginpage[1].clear()
            loginpage[1].send_keys(self.psw)
            self.driver.find_element_by_class_name("android.widget.button").click()
        except:
            pass

    def test02_addrod(self):
        time.sleep(2)
        # 安装工单
        self.driver.find_elements_by_class_name("android.view.view")[5].click()
        # 添加杆号
        self.driver.find_element_by_accessibility_id("杆号管理").click()
        self.driver.find_element_by_accessibility_id("添加杆号").click()
        time.sleep(1)
        self.driver.find_elements_by_class_name("android.widget.edittext")[0].send_keys(self.rodnum)  # 输入杆号
        self.driver.find_element_by_accessibility_id("确定").click()
        time.sleep(2)
        # 返回
        self.driver.find_elements_by_class_name("android.view.view")[1].click()
        time.sleep(1)

    def test03_addbase(self):
        self.rodnum = Config().get('rodnum')
        self.basenum = Config().get('basenum')
        time.sleep(1)
        # 添加基站
        self.driver.find_element_by_accessibility_id("基站管理").click()
        self.driver.find_element_by_accessibility_id("添加基站").click()
        time.sleep(2)
        # 添加手机图片
        self.driver.find_element_by_accessibility_id("add_picture").click()
        time.sleep(1)
        self.driver.tap([(366,1812),])
        time.sleep(2)
        self.driver.find_element_by_name("相册").click()
        self.driver.find_elements_by_id("com.miui.gallery:id/pick_num_indicator")[1].click()  # 选第二张图
        # 输入信息
        self.driver.find_elements_by_class_name("android.widget.edittext")[1].send_keys(self.basenum)  # 输入基站物理编号
        self.driver.find_elements_by_class_name("android.widget.edittext")[2].send_keys(self.rodnum)  # 输入杆号
        self.driver.find_element_by_accessibility_id("查询杆号").click()
        time.sleep(1)
        self.tap([(366,1812),])
        time.sleep(2)
        self.swipe(100, 1000, 100, 50,0)  # 滑动
        self.find_elements_by_class_name("android.widget.edittext")[5].send_keys("v 1.0")  # 软件版本
        self.find_element_by_accessibility_id("确定").click()
        time.sleep(2)
        # 判断
        try:
            assert self.driver.find_elements_by_class_name("android.view.view")[4].get_attribute("name") == self.basenum, "新增基站未找到"
            print("新增基站成功")
        except AssertionError,msg:
            print msg

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)