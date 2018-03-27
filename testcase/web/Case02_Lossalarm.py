# coding:utf-8
import sys
import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pageobject.Page_Login import Page_Login
from pageobject.Page_main import Page_main
from utils.config import Config
from utils.log1 import Log
import time
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()
@ddt.ddt
class addcompany(unittest.TestCase):
    u'''管理员登录'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.A = Page_main(self.driver)
        self.l.open(self.url)

    def test01_login(self):
        u'''管理员登录'''
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginAccount_loc, "系统管理员", "-------管理员登录  失败-------"))
        log.info("-------管理员登录  用例结束-------")

    def test02_add(self):
        u'''电动车丢失报警，新增'''
        time.sleep(2)
        self.driver.find_element("xpath", ".//*[@id='mainlayout_body']/div[1]/div/div[2]/ul/li[2]/a" ).click()   # 横向导航菜单：电动车管理
        ifr = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr[1])
        time.sleep(1)
        self.driver.find_element("xpath", ".//*[@id='accordion']/div[2]/div[1]/div[1]").click()    # 电动车管理
        time.sleep(1)
        self.driver.find_element("xpath", ".//*[@id='accordion']/div[2]/div[2]/ul/li[3]/a").click()    # 电动车丢失报警
        ifr1 = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr1[1])


        time.sleep(2)
        # 新增按钮
        self.driver.find_element("xpath", ".//*[@id='carFileSearch']/button[2]").click()
        time.sleep(2)
        self.driver.find_element("id", 'chipCode').send_keys("65523")  # 芯片编号
        self.driver.find_elements("class name", 'combo-arrow')[1].click()  # 案发时间
        self.driver.find_element("link text", u'今天').click()  # 案发时间-今天
        self.driver.find_elements("class name", 'combo-arrow')[3].click()  # 区域-市
        self.driver.find_element("id", '_easyui_combobox_i15_0').click()  # 下拉选第一项
        self.driver.find_elements("class name", 'combo-arrow')[4].click()  # 区域-区
        self.driver.find_element("id", '_easyui_combobox_i14_0').click()  # 下拉选第一项
        self.driver.find_element("id", 'save_addPetFile').click() # 保存
        self.driver.find_element("link text", u'确定').click()  # 确定


        self.driver.switch_to.default_content()
    #     self.psw = Config().get('PASSWORD')
    #     self.l.login(self.username, self.psw)
    #     # 判断是否登录成功
    #     self.assertTrue(self.l.is_text_in_element(self.A.loginAccount_loc, "系统管理员", "-------新增备案登记 失败-------"))
    #     log.info("-------新增备案登记 用例结束-------")

    # @classmethod
    # def tearDownClass(self):
    #     # 关闭浏览器
    #     self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)