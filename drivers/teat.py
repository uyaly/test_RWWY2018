# coding:utf-8
from selenium import webdriver
from utils.file_reader import ExcelUtil
# re非贪婪模式，正则匹配
import re
driver = webdriver.Firefox()
driver.get("http://192.168.3.183:14010/iot/login")
# selenium的page_source方法可以直接返回页面源码
page = driver.page_source
print page
readXLS = ExcelUtil()
str = readXLS.dict_data()
# str[i] =
# "非贪婪匹配,re.S('.'匹配字符,包括换行符)"
# url_list = re.findall('href=\"(.*?)\"', page, re.S)
# url_all = []
# for url in url_list:
#     if "http" in url:
#         # print url
#         url_all.append(url if not isinstance(url, unicode) else url.encode('utf-8'))
#         # url_all.append(url)
# # 最终的url集合
# print url_all


def dingwei(driver,str1):
    u'''定位功能方法'''
    driver.implicitly_wait(10)
    str2=str1
    panduan = re.findall(r'\xa0(.*?)=', str2)
    for i in range(len(panduan)):
        panduan[i]=panduan[i].split(' ')[-1]
    daan = re.findall(r'="(.*?)"',str2)
    try:
        id = re.findall(r'id="(.*?)"',str2)[0]
        elements = driver.find_elements_by_id(id)

        for i in elements:
            for j in range(len(panduan)):
                if i.get_attribute(panduan[j]) != daan[j]:
                    if panduan[j] == 'value' or panduan[j] == 'readonly' or panduan[j]=='title':
                        continue
                    else:
                        print u'属性名:',panduan[j]
                        print u'id定位:',i.get_attribute(panduan[j]),'XXX',daan[j]
                        break
            else:
                print u'id成功定位: ',id
                return i
    except Exception,e:
        print u'id未找到'


    try:
        name = re.findall(r'name="(.*)"',str2)[0]
        elements = driver.find_elements_by_name(name)
        for i in elements:
            for j in range(len(panduan)):
                if i.get_attribute(panduan[j]) != daan[j]:
                    if panduan[j] == 'value':
                        continue
                    else:
                        print u'属性名:', panduan[j]
                        print u'name定位',i.get_attribute(panduan[j]), 'XXX', daan[j]
                        break
            else:
                print u'name成功定位: ', name
                return i
    except Exception, e:
        print U'name未找到'

    try:
        link_text = re.findall(r'>(.*)<',str2)[0]
        elements = driver.find_elements_by_link_text(link_text)
        for i in elements:
            for j in range(len(panduan)):
                if i.get_attribute(panduan[j]) != daan[j]:
                    if panduan[j] == 'value':
                        continue
                    else:
                        print u'属性名:', panduan[j]
                        print u'link_text定位:',i.get_attribute(panduan[j]), 'XXX', daan[j]
                        break
            else:
                print u'link_text成功定位: ', link_text
                return i
    except Exception, e:
        print u'link_text未找到'

    try:
        class_name = re.findall(r'class="(.*?)"', str2)[0].split(' ')[-1]
        elements = driver.find_elements_by_class_name(class_name)
        print elements
        for i in elements:
            for j in range(len(panduan)):
                if i.get_attribute(panduan[j]) != daan[j]:
                    if panduan[j] == 'value':
                        continue
                    else:
                        print u'属性名:', panduan[j]
                        print u'class_name定位:',i.get_attribute(panduan[j]), 'XXX', daan[j]
                        break
            else:
                print u'class_name成功定位: ', class_name
                return i
    except Exception, e:
        print u'class_name未找到'

    print u'这个控件实在是找不到了....'
    exit()

if __name__ == '__main__':
    dingwei(driver,page)