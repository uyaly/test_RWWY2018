# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class Page_main(ly):
    ElectricVehicle_manage = ("xpath", ".//*[@id='mainlayout_body']/div[1]/div/div[2]/ul/li[2]/a" )   # 横向导航菜单：电动车管理
    ElectricVehicle_manage1 = ("xpath", ".//*[@id='accordion']/div[2]/div[1]/div[1]")    # 电动车管理
    ElectricVehicle_record = ("xpath", ".//*[@id='accordion']/div[2]/div[2]/ul/li[2]/a")    # 电动车备案登记
    ElectricVehicle_LossAlarm = ("xpath", ".//*[@id='accordion']/div[2]/div[2]/ul/li[3]/a")    # 电动车丢失报警
    ElectricVehicle_Blacklist = ("xpath", ".//*[@id='accordion']/div[2]/div[2]/ul/li[4]/a")    # 丢失电动车