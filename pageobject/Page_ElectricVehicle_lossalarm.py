# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class ElectricVehicle_lossalarm(ly):
    # 定位器，定位页面元素
    # 列表按钮
    add_button = ("xpath", ".//*[@id='carFileSearch']/button[2]")
    query_button = ("xpath", ".//*[@id='carFileSearch']/button[1]")
    # 新增页面
    telephone_loc = ("id", 'telephoneForRegister')  # 手机号
    queue_loc = ("class name", 'combo-text')  # 下拉队列
    region21_loc = ("id", '_easyui_combobox_i15_0')  # 区域-市,下拉选第一项
    region31_loc = ("id", '_easyui_combobox_i14_0')  # 区域-区,下拉选第一项
    occurdate1_loc = ("link text", u'今天')  # 购车日期,今天
    save_button = ("id", 'save_addPetFile')  # 保存
    confirm_button = ("link text", u'确定')  # 确定

    # 查询
    chipid_loc = ("xpath", ".//*[@id='add_carFile']/div/div/form/span[1]/input[1]")
    status_loc = ("xpath", ".//*[@id='carFileSearch']/span[5]/input[1]")

    status1_loc = ("class name", "combobox-item")  # 状态选项
    # 删除一行
    # row_loc = ("class name", "datagrid-row")    # 待删行
    # 流程
    operate1_loc = ("link text", u"确认报警")   # 操作
    operate2_loc = ("link text", u"确认接警")   # 操作
    operate3_loc = ("link text", u"查找车辆")   # 操作
    operate4_loc = ("link text", u"涉案人员")   # 操作
    # 弹出窗口文字
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


    def click_save(self):
        '''点击保存'''
        self.click(self.save_button)

    def click_confirm(self):
        '''点击确定'''
        self.click(self.confirm_button)

    def click_query(self):
        '''点击确定'''
        self.click(self.query_button)

    def input_chipid(self, chipId):
        '''查询关键字输入芯片'''
        self.find_element(self.chipid_loc).sendkeys(chipId)

    def select_status(self, status):
        '''查询关键字选择报警状态'''
        self.find_element(self.status_loc).click()
        su = self.find_elements(self.status_loc1)
        for i in range(len(su)):
            if su[i].text == status:
                su[i].click()  # 选中状态对应项

    def operate(self, operate):
        self.click(self.operate1_loc)



