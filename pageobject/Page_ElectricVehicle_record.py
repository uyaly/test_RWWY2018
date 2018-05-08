# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class ElectricVehicle_record(ly):
    # 定位器，定位页面元素
    # 列表按钮
    add_button = ("xpath", ".//*[@id='searchForm']/button[3]")
    del_button = ("xpath", ".//*[@id='searchForm']/button[4]")
    # 新增页面
    telephone_loc = ("id", 'telephoneForRegister')  # 手机号
    chipId_loc = ("name", 'chipId')  # 芯片编号

    queue_loc = ("class name", "combo-arrow")  # 下拉队列
    Installpoint1_loc = ("id", '_easyui_combobox_i15_0')  # 安装点下拉选第一项
    region21_loc = ("id", '_easyui_combobox_i21_0')  # 区域-市,孝感
    region31_loc = ("id", '_easyui_combobox_i22_0')  # 区域-区,安陆
    # region21_loc = ("id", '_easyui_combobox_i21_7')  # 区域-市,武汉
    # region31_loc = ("id", '_easyui_combobox_i22_4')  # 区域-区,洪山

    platenumber_loc = ("name", 'vehicleIdmunber')  # 车牌号
    VIN_loc = ("name", 'frameCode')  # 车架号
    type1_loc = ("id", '_easyui_combobox_i16_0')  # 车辆类型,下拉选第一项
    brand1_loc = ("id", '_easyui_combobox_i18_0')  # 车辆品牌,下拉选第一项
    color1_loc = ("id", '_easyui_combobox_i17_0')  # 车辆颜色,下拉选第一项
    purchasedate1_loc = ("link text", u'今天')  # 购车日期,今天
    save_button = ("id", 'saveBtn')  # 保存
    confirm_button = ("link text", u'确定')  # 确定

    # 删除一行
    row_loc = ("class name", "datagrid-row")    # 待删行

    # 弹出窗口文字
    alert_text = ("class name", "messager-question")

    def click_add(self):
        '''点击新建'''
        self.click(self.add_button)

    def click_del(self):
        '''点击删除'''
        self.click(self.del_button)

    def input_telephone(self, telephone):
        '''输入手机号'''
        self.send_keys(self.telephone_loc, telephone)

    def input_chipId(self, chipId):
        '''输入芯片编号'''
        self.send_keys(self.chipId_loc, chipId)

    def select_Installpoint(self):
        '''选择安装点'''
        self.find_elements(self.queue_loc)[5].click()
        self.click(self.Installpoint1_loc)


    def select_region2(self):
        '''选择区域-市'''
        self.find_elements(self.queue_loc)[7].click()
        self.click(self.region21_loc)

    def select_region3(self):
        '''选择区域-区'''
        self.find_elements(self.queue_loc)[8].click()
        self.click(self.region31_loc)

    def input_platenumber(self, platenumber):
        '''输入车牌号'''
        self.send_keys(self.platenumber_loc, platenumber)

    def input_VIN(self, VIN):
        '''输入车架号'''
        self.send_keys(self.VIN_loc, VIN)

    def select_type(self):
        '''选择车辆类型'''
        self.find_elements(self.queue_loc)[9].click()
        self.click(self.type1_loc)

    def select_brand(self):
        '''选择车辆品牌'''
        self.find_elements(self.queue_loc)[10].click()
        self.click(self.brand1_loc)

    def select_purchasedate(self):
        '''选择购车日期'''
        self.find_elements(self.queue_loc)[11].click()
        self.click(self.purchasedate1_loc)

    def select_color(self):
        '''选择车辆颜色'''
        self.find_elements(self.queue_loc)[12].click()
        self.click(self.color1_loc)

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


    def click_save(self):
        '''点击保存'''
        self.click(self.save_button)

    def click_confirm(self):
        '''点击确定'''
        self.click(self.confirm_button)

    # def input_account(self, username):
    #     '''输入查询账号'''
    #     self.send_keys(self.account_loc, username)
