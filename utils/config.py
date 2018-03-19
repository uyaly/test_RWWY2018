# coding:utf-8
import os
from utils.file_reader import YamlReader
from utils.file_reader import ExcelUtil
import xlrd

BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
CONFIG_FILE = BASE_PATH + '\\config\\conf.yaml'
DATA_FILE = BASE_PATH + '\\data\\testdata.xlsx'
DRIVER_PATH = BASE_PATH + '\\drivers\\'
LOG_PATH = BASE_PATH + '\\report\\'
sheetName = "original"
element = "HZ_ZSHY_original"
class Config:
    u'''读取配置'''
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)

class XlsData:
    u'''读取xls数据'''
    def __init__(self):
        xlsdata = ExcelUtil(DATA_FILE, sheetName)
        print xlsdata.dict_data()

    def get(self, element, index=0):
        for index in range(len(self.XlsData)):
            if self.XlsData[index] == element:
                print self.XlsData[index+1]
            index = index + 1