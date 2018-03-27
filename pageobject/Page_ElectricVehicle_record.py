# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class Page_main(ly):
    # 定位器，定位页面元素
    # 列表按钮
    add_button = ("xpath", ".//*[@id='searchForm']/button[2]")
    # 新增页面
    telephone = ("id", 'telephoneForRegister')  # 手机号
    chipId = ("name", 'chipId')  # 芯片编号
    Installpoint = ("class name", 'combo-arrow')  # 安装点
    Installpoint1 = ("id", '_easyui_combobox_i15_0')  # 安装点下拉选第一项
    region2 = ("class name", 'combo-arrow')  # 区域-市
    region21 = ("id", '_easyui_combobox_i21_0')  # 下拉选第一项
    region3 = ("class name", 'combo-arrow')  # 区域-区
    region31 = ("id", '_easyui_combobox_i22_0')  # 下拉选第一项
    platenumber = ("name", 'vehicleIdmunber')  # 车牌号
    VIN = ("name", 'frameCode')  # 车架号
    type = ("class name", 'combo-arrow')  # 车辆类型
    type1 = ("id", '_easyui_combobox_i16_0')  # 下拉选第一项
    brand = ("class name", 'combo-arrow')  # 车辆品牌
    brand1 = ("id", '_easyui_combobox_i18_0')  # 下拉选第一项
    color = ("class name", 'combo-arrow')  # 车辆颜色
    color1 = ("id", '_easyui_combobox_i17_0')  # 下拉选第一项
    purchasedate = ("class name", 'combo-arrow')  # 购车日期
    purchasedate1 = ("link text", u'今天')  # 购车日期-今天
    save_button = ("id", 'saveBtn')  # 保存
    confirm_button = ("link text", u'确定')  # 确定

    # 弹出窗口文字
    alert_text = ("class name", "messager-body")

    def click_add(self):
        '''新建'''
        self.click(self.add_button)

    def click_save(self):
        '''保存'''
        self.click(self.save_button)

    def click_confirm(self):
        '''确定'''
        self.click(self.confirm_button)

    # def input_account(self, username):
    #     '''输入查询账号'''
    #     self.send_keys(self.account_loc, username)
