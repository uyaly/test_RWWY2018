# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class Page_main(ly):
    # 定位器，定位页面元素
    loginAccount_loc = ("class name", 'userName')
    # 功能按钮，增删改查
    ADD_Button = ("class name", 'addBtn')
    DEL_Button = ("class name", 'deleteBtn')
    EDIT_Button = ("class name", 'editBtn')
    QUERY_Button = ("class name", 'query')
    # 删除一行
    row_loc = ("class name", "datagrid-row")    # 待删行
    # save_button = ("id", 'saveBtn')    # 保存
    # cancel_button = ("id", 'cancelBtn')    # 取消
    # ok_button = ("link text", '确定')    # 确定
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
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(self.loginAccount_loc))

        if (module == "电动车备案登记"):
        #  '''横向导航菜单：电动车管理'''
            self.click(self.ElectricVehicle_manage)
            self.click(self.ElectricVehicle_record)

        elif (module == "电动车丢失报警"):
            self.click(self.ElectricVehicle_manage)
            self.click(self.ElectricVehicle_LossAlarm)

        elif (module == "丢失电动车"):
            self.click(self.ElectricVehicle_manage)
            self.click(self.ElectricVehicle_Blacklist)

        else:
            pass

    def LoginOut(self):
        '''退出'''
        self.click(self.loginout_loc)

    def add(self):
        '''点击新增按钮'''
        self.send_keys_botton(self.ADD_Button, Keys.ENTER)

    def delete(self):
        '''点击删除按钮'''
        self.send_keys_botton(self.DEL_Button, Keys.ENTER)

    def edit(self):
        '''点击修改按钮'''
        self.send_keys_botton(self.EDIT_Button, Keys.ENTER)

    def query(self):
        '''点击查询按钮'''
        self.send_keys_botton(self.QUERY_Button, Keys.ENTER)




    def select_row(self, username):
        '''选中列表待删行'''
        b = False
        row = self.find_elements(self.row_loc)
        try:
            for n in range(len(row)):
                # print row[n].text
                if username in row[n].text:
                    row[n].click()
                    b = True
                    return b
            if b == False:
                return False
        except Exception as msg:
            print("Error:%s" % msg)

    # def select_row(self, username):
    #     '''查找列表中的初期额度'''
    #     b = False
    #     row = self.find_elements(self.row_loc)
    #     try:
    #         for n in range(len(row)):
    #             # print row[n].text
    #             if username in row[n].text:
    #                 row[n].click()
    #                 b = True
    #                 return b
    #         if b == False:
    #             return False
    #     except Exception as msg:
    #         print("Error:%s" % msg)

    def click_save(self):
        '''保存'''
        self.click(self.save_button)

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)

    def input_account(self, username):
        '''输入查询账号'''
        self.send_keys(self.account_loc, username)
