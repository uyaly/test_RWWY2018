# coding:utf-8
import os
from utils.file_reader import YamlReader
from utils.file_reader import ExcelUtil
import xlrd
import ddt

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

@ddt.ddt
class XlsData:
    u'''读取xls数据'''
    def __init__(self):
        self.xlsdata = ExcelUtil(DATA_FILE, sheetName)
        self.testData = self.xlsdata.dict_data()
        print self.testData

    def get(self, element, index=0):
        # print "列表长度：" + str(len(self.xlsdata))
        # for index in self.testData:
        #     if self.testData[index] == element:
        #         print self.testData[index+1]
        return self.testData[index].get(element)
# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    # unittest.main(verbosity=2)
    XlsData.get()