# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class Page_main(ly):
    # 定位器，定位页面元素
    loginAccount_loc = ("class name", 'userName')
    logout_loc = ("id", 'logout')
    # save_button = ("id", 'saveBtn')    # 保存
    # cancel_button = ("id", 'cancelBtn')    # 取消
    ok_button = ("link text", '确定')    # 确定
    # 模块
    ElectricVehicle_Monitor = ("xpath", ".//*[@id='mainlayout_body']/div[1]/div/div[2]/ul/li[2]/a")   # 横向导航菜单：电动车管理
    ElectricVehicle_manage = ("xpath", ".//*[@id='accordion']/div[2]/div[1]/div[1]")    # 电动车管理
    ElectricVehicle_record = ("xpath", ".//*[@id='accordion']/div[2]/div[2]/ul/li[2]/a")    # 电动车备案登记
    ElectricVehicle_LossAlarm = ("xpath", ".//*[@id='accordion']/div[2]/div[2]/ul/li[3]/a")    # 电动车丢失报警
    ElectricVehicle_Blacklist = ("xpath", ".//*[@id='accordion']/div[2]/div[2]/ul/li[4]/a")    # 丢失电动车

    def Into_ElectricVehicle_manage(self):
        '''横向导航菜单：电动车管理'''
        self.click(self.ElectricVehicle_Monitor)

    # 查询
    account_loc = ("id", 'a_query')
    # 弹出窗口文字
    alert_text = ("class name", "messager-body")

    def IntoModule(self, module):
        '''进入模块'''
        # 等待时长10秒，默认0.5秒询问一次
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(self.loginAccount_loc))

        if (module == "电动车备案登记"):
        #  '''横向导航菜单：电动车管理'''
            self.click(self.ElectricVehicle_manage)
            time.sleep(1)
            self.click(self.ElectricVehicle_record)

        elif (module == "电动车丢失报警"):
            self.click(self.ElectricVehicle_manage)
            time.sleep(1)
            self.click(self.ElectricVehicle_LossAlarm)

        elif (module == "丢失电动车"):
            self.click(self.ElectricVehicle_manage)
            time.sleep(1)
            self.click(self.ElectricVehicle_Blacklist)

        else:
            pass

    def logout(self):
        '''退出'''
        self.move_to_element(self.loginAccount_loc)
        time.sleep(2)
        self.click(self.logout_loc)

    def click_save(self):
        '''保存'''
        self.click(self.save_button)

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)

    def input_account(self, username):
        '''输入查询账号'''
        self.send_keys(self.account_loc, username)
