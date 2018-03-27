# coding:utf-8
import sys
import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
        log.info("-------管理员登录  用例结束-------")

    def test02_add(self):
        u'''电动车备案登记，新增'''
        self.Page_main.Into_ElectricVehicle_manage()
        ifr = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr[1])
        self.Page_main.IntoModule("电动车备案登记")
        ifr1 = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(ifr1[1])
        time.sleep(2)
        # 新增按钮
        self.EVRecord.click_add()
        # 新增页面输入项
        # time.sleep(2)
        self.EVRecord.input_telephone(Config().get('PHONE'))  # 手机号
        self.EVRecord.input_chipId(Config().get('chipId'))  # 芯片编号
        self.EVRecord.select_Installpoint()  # 安装点
        self.EVRecord.select_region2()  # 区域-市
        self.EVRecord.select_region3()  # 区域-区
        self.EVRecord.input_platenumber(Config().get('PLATENUMBER'))   # 车牌号
        self.EVRecord.input_VIN(Config().get('PLATENUMBER'))   # 车架号
        self.EVRecord.select_type()   # 车辆类型
        self.EVRecord.select_brand()   # 车辆品牌
        self.EVRecord.select_color()   # 车辆颜色
        self.EVRecord.select_purchasedate()   # 购车日期
        self.EVRecord.click_save()   # 保存
        # 判断是否新建成功
        # self.assertTrue(self.Login.is_text_in_element(self.Page_main.alert_text, "新增成功", str(self.Login.get_text(self.Page_main.alert_text))))
        print self.Page_main.alert_text

        # 确定
        # self.EVRecord.click_confirm()   # 确定
        log.info('-------新增公司    用例结束-------')
        # self.driver.switch_to.default_content()



    # @classmethod
    # def tearDownClass(self):
    #     # 关闭浏览器
    #     self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)