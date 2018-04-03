# coding:utf-8
import sys
import unittest
import ddt
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from pageobject.Page_main import Page_main
from pageobject.Page_ElectricVehicle_record import ElectricVehicle_record
from utils.config import Config
from utils.log1 import Log
import time
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()
@ddt.ddt
class add_ElectricVehicle_record(unittest.TestCase):
    u'''新增电动车备案登记'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.Login = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.Login.open(self.url)
        self.Page_main = Page_main(self.driver)
        self.EVRecord = ElectricVehicle_record(self.driver)

    def test01_login(self):
        u'''管理员登录'''
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.Login.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.Login.is_text_in_element(self.Page_main.loginAccount_loc, "系统管理员", "-------管理员登录  失败-------"))
        log.info("-------管理员登录      用例结束-------")

    def test02_DEL(self):
        u'''电动车备案登记，删除'''
        self.chipId = Config().get('CHIPID')
        self.Page_main.Into_ElectricVehicle_manage()
        ifr = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr[1])
        time.sleep(2)
        self.Page_main.IntoModule("电动车备案登记")
        ifr1 = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr1[1])
        time.sleep(2)
        alertmsg = ''
        try:
            self.EVRecord.select_row(self.chipId)
            self.EVRecord.click_del()
            self.Page_main.click_ok()
            time.sleep(2)
            # 判断是否新建成功，记录alert文字
            alertmsg =  self.Login.get_text(self.Page_main.alert_text)
            # print str(alertmsg)
            self.Page_main.click_ok()
        except:
            print "未找到芯片：" + self.chipId
        # print str(alertmsg)
        self.assertTrue(alertmsg == u'操作成功\n确定', "-------备案登记删除  失败-------")
        log.info("-------备案登记删除  用例结束-------")

    # def test03_logout(self):
    #     u'''管理员登出'''
    #     time.sleep(5)
    #     self.Page_main.logout()
    #     # 判断是否登出成功
    #     time.sleep(2)
    #     self.assertTrue(self.Login.is_text_in_element(self.Login.title_loc, "登录", "-------管理员登出     失败-------"))
    #     log.info("-------管理员登出      用例结束-------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)