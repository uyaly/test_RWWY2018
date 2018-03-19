# coding:utf-8

import yaml
import os
import csv
import xlrd
class YamlReader:
    u'''封装一个YamlReader类'''

    def __init__(self, yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            # raise FileNotFoundError('文件不存在！')
            print '文件不存在'
        self._data = None

    @property
    def data(self):
        if self._data:
            return self._data
        else:
            with open(self.yaml, 'rb')as f:
                return list(yaml.safe_load_all(f))

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小亍1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
                return r

if __name__ == "__main__":
    # 注意：此代码if以上的勿乱改，调用此方法叧需修改两个参数，一个是excelPath存放xlsx的路径，另外一个是sheetName的值
    # filePath = r"D:\PycharmProjects\test_hpk2017\data\testdata.xlsx"
    # sheetName = "original"
    # data = ExcelUtil(filePath, sheetName)
    # print data.dict_data()
    pass