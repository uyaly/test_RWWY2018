# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class Page_main(ly):
    # 定位器，定位页面元素
    telephone = ("id", 'telephoneForRegister')
    name = ("id", 'ilinkappUserName')
    id = ("class name", 'e_ipt')
    chipId = ("name", 'chipId')
    add = ("id", 'address')




    # 弹出窗口文字
    alert_text = ("class name", "messager-body")

    def click_save(self):
        '''保存'''
        self.click(self.save_button)

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)

    def input_account(self, username):
        '''输入查询账号'''
        self.send_keys(self.account_loc, username)
