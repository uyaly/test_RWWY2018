# coding:utf-8
import csv,xlrd
from selenium import webdriver
import time

file_name = r'D:\PycharmProjects\test_hpk2017\data\testdata.xlsx'

def getCsv(file_name):
    rows=[]
    with open(file_name, 'rb') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            rows.append(row)
            return rows

def getExcel(rowValue, colValue, file_name):
    '''
    :param rowValue:表格的行
    :param colValue:表格的列
    :param file_name:excel文件
    :return:
    '''
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    return sheet.cell_value(rowValue, colValue)

def getDdExcel(File_name):
    rows = []
    book = xlrd.open_workbook(File_name)
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
        return rows

def getData(rowValue, colname):
    '''
    :param File_name: excel文件
    :param rowValue: 表格的行
    :param element: 表格的列
    :return:
    '''
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for colValue in range(0, sheet.ncols):
        if sheet.cell_value(0, colValue) == colname:
            return sheet.cell_value(rowValue, colValue)
        colValue = colValue + 1

# 获取返回的错误信息
def getText(driver):
    return driver.find_element_by_xpath("").text


# 执行测试主函数
if __name__ == '__main__':
    # print getDdExcel(file_name)
    # print getExcel(0, 0, file_name)
    # print getData(file_name, 1, "HZ_ZSHY_original")
    pass