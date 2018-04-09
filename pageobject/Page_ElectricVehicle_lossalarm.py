# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class ElectricVehicle_lossalarm(ly):
    # 定位器，定位页面元素
    # 列表功能按钮
    add_button = ("xpath", ".//*[@id='carFileSearch']/button[2]")
    query_button = ("xpath", ".//*[@id='carFileSearch']/button[1]")

    # 新增页面输入项
    telephone_loc = ("id", 'telephoneForRegister')  # 手机号
    queue_loc = ("class name", 'combo-text')  # 下拉队列
    region21_loc = ("id", '_easyui_combobox_i15_7')  # 区域-市,武汉
    region31_loc = ("id", '_easyui_combobox_i14_4')  # 区域-区,洪山
    # region21_loc = ("id", '_easyui_combobox_i15_10')  # 区域-市,孝感
    # region31_loc = ("id", '_easyui_combobox_i14_0')  # 区域-区,安陆

    occurdate1_loc = ("link text", u'今天')  # 购车日期,今天

    # 新增页面按钮
    save_button = ("id", 'save_addPetFile')  # 保存
    confirm_button = ("link text", u'确定')  # 确定

    # 查询
    chipid_loc = ("xpath", ".//*[@id='carFileSearch']/span[2]/input[1]")
    status_loc = ("xpath", ".//*[@id='carFileSearch']/span[5]/input[1]")
    status1_loc = ("class name", "combobox-item")  # 状态子选项

    # 操作流程
    operate_loc = ("xpath", ".//*[@id='datagrid-row-r1-2-0']/td[16]/div/a[2]")   # 操作链接，主流程均为第二个

    # 查找车辆
    searchsave_button = ("id", 'save_serachCar')  # 保存
    back_Radio = ("xpath", ".//*[@id='serachCar']/div/div/label[2]")  # 单选-车辆已找回
    notback_Radio = ("xpath", ".//*[@id='serachCar']/div/div/label[3]")  # 单选-车辆未找回
    notback_loc = ("xpath", ".//*[@id='box_02']/span/input[1]")  # 单选-车辆未找回
    back_loc = ("xpath", ".//*[@id='box_01']/span/input[1]")  # 单选-车辆未找回
    back3_loc = ("id", '_easyui_combobox_i22_2')  # 已找回子选项
    notback1_loc = ("id", '_easyui_combobox_i23_0')  # 未找回子选项

    # 新增弹出窗口文字
    alert_text = ("class name", "messager-question")

    def click_add(self):
        '''点击新建'''
        self.click(self.add_button)

    def input_chipId(self, chipId):
        '''输入芯片编号'''
        self.find_elements(self.queue_loc)[2].send_keys(chipId)

    def select_region2(self):
        '''选择区域-市'''
        self.find_elements(self.queue_loc)[5].click()
        self.click(self.region21_loc)

    def select_region3(self):
        '''选择区域-区'''
        self.find_elements(self.queue_loc)[6].click()
        self.click(self.region31_loc)

    def select_occurdate(self):
        '''选择案发日期'''
        # self.select_by_index(self.purchasedate_loc[11], num)
        self.find_elements(self.queue_loc)[3].click()
        self.click(self.occurdate1_loc)

    def select_row(self, chipId):
        '''查找列表中的一行'''
        b = False
        row = self.find_elements(self.row_loc)
        try:
            for n in range(len(row)):
                # print row[n].text
                if chipId in row[n].text:
                    row[n].click()
                    b = True
                    return b
            if b == False:
                return False
        except Exception as msg:
            print("Error:%s" % msg)

    # 点击功能按钮
    def click_save(self):
        '''点击保存'''
        self.click(self.save_button)

    def click_confirm(self):
        '''点击确定'''
        self.click(self.confirm_button)

    def click_query(self):
        '''点击查询'''
        self.click(self.query_button)

    #  查询关键字
    def input_chipid(self, chipId):
        '''查询关键字输入芯片'''
        self.find_element(self.chipid_loc).clear()
        self.find_element(self.chipid_loc).send_keys(chipId)

    def select_status(self, status):
        '''查询关键字选择报警状态'''
        self.find_element(self.status_loc).click()
        su = self.find_elements(self.status1_loc)
        for i in range(len(su)):
            if su[i].text == status:
                su[i].click()  # 选中状态对应项
    #  查找车辆
    def operate(self):
        self.click(self.operate_loc)

    def search(self, search):
        if (search == "已找回"):
            self.click(self.back_Radio)
            self.click(self.back_loc)
            self.click(self.back3_loc)
        else:
            self.click(self.notback_Radio)
            self.click(self.notback_loc)
            self.click(self.notback1_loc)

    def click_searchsave(self):
        '''查找车辆界面点击保存按钮'''
        self.click(self.searchsave_button)

    #  涉案人员



