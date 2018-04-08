# coding:utf-8
import sys
import unittest
import ddt
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from pageobject.Page_main import Page_main
from pageobject.Page_ElectricVehicle_lossalarm import ElectricVehicle_lossalarm
from utils.config import Config
from utils.log1 import Log
import time
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()
@ddt.ddt
class ElectricVehicle_lossalarm_add(unittest.TestCase):
    u'''走流程,电动车丢失报警'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.Login = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.Login.open(self.url)
        self.Page_main = Page_main(self.driver)
        self.EVlossalarm = ElectricVehicle_lossalarm(self.driver)

    def test01_login(self):
        u'''管理员登录'''
        self.username = Config().get('ADMIN')
        self.name = Config().get('ADMINNAME')
        self.psw = Config().get('PASSWORD')
        self.Login.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.Login.is_text_in_element(self.Page_main.loginAccount_loc, self.name, "-------管理员登录          失败-------"))
        log.info("-------管理员登录      用例结束-------")
        self.Page_main.Into_ElectricVehicle_manage()
        ifr = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr[1])
        time.sleep(2)
        self.Page_main.IntoModule("电动车丢失报警")
        ifr1 = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr1[1])
        time.sleep(2)

    def test02_ConfirmAlarm(self):
        u'''电动车丢失报警，对【未处理】状态做【确认报警】'''
        ChipID = Config().get('CHIPID')
        self.EVlossalarm.input_chipid(ChipID)
        self.EVlossalarm.select_status("未接警")
        self.EVlossalarm.click_query()
        time.sleep(1)
        self.EVlossalarm.operate()  # 【确认报警】
        alertmsg = ''
        try:
            # 判断是否新建成功，记录alert文字
            alertmsg = self.Login.get_text(self.Page_main.alert_text)
            self.EVlossalarm.click_confirm()   # 确定
        except:
            pass
        self.assertIn( u'确认报警成功', alertmsg, alertmsg)
        log.info('-------确认报警        用例结束-------')

    def test03_ConfirmAccept(self):
        u'''电动车丢失报警，对【已确认】状态做【确认接警】'''
        ChipID = Config().get('CHIPID')
        self.EVlossalarm.input_chipid(ChipID)
        self.EVlossalarm.select_status("已确认")
        self.EVlossalarm.click_query()
        self.driver.execute_script("window.scrollTo(1000,400)")
        time.sleep(1)
        self.EVlossalarm.operate()  # 【确认接警】
        alertmsg = ''
        try:
            # 判断是否新建成功，记录alert文字
            alertmsg = self.Login.get_text(self.Page_main.alert_text)
            self.EVlossalarm.click_confirm()   # 确定
        except:
            pass
        self.assertIn( u'确认接警成功', alertmsg, alertmsg)
        log.info('-------确认接警        用例结束-------')

    def test04_SearchNotBack(self):
        u'''电动车丢失报警，对【已接警】状态做【查找车辆】【未找回】'''
        ChipID = Config().get('CHIPID')
        self.EVlossalarm.input_chipid(ChipID)
        self.EVlossalarm.select_status("已接警")
        self.EVlossalarm.click_query()
        self.driver.execute_script("window.scrollTo(1000,400)")
        time.sleep(1)
        self.EVlossalarm.operate()  # 【查找车辆】
        time.sleep(1)
        self.EVlossalarm.search("未找回")
        self.EVlossalarm.click_searchsave()
        alertmsg = ''
        try:
            # 判断是否新建成功，记录alert文字
            alertmsg = self.Login.get_text(self.Page_main.alert_text)
            self.EVlossalarm.click_confirm()   # 确定
        except:
            pass
        self.assertIn( u'处理成功', alertmsg, alertmsg)
        log.info('-------查找车辆-未找回 用例结束-------')

    def test05_SearchBack(self):
        u'''电动车丢失报警，对【已接警】状态做【查找车辆】【已找回】'''
        ChipID = Config().get('CHIPID')
        self.EVlossalarm.input_chipid(ChipID)
        self.EVlossalarm.select_status("已接警")
        self.EVlossalarm.click_query()
        self.driver.execute_script("window.scrollTo(1000,400)")
        time.sleep(1)
        self.EVlossalarm.operate()  # 【查找车辆】
        time.sleep(1)
        self.EVlossalarm.search("已找回")
        self.EVlossalarm.click_searchsave()
        alertmsg = ''
        try:
            # 判断是否新建成功，记录alert文字
            alertmsg = self.Login.get_text(self.Page_main.alert_text)
            self.EVlossalarm.click_confirm()   # 确定
        except:
            pass
        self.assertIn( u'处理成功', alertmsg, alertmsg)
        log.info('-------查找车辆-已找回 用例结束-------')

    # @classmethod
    # def tearDownClass(self):
    #     # 关闭浏览器
    #     self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)