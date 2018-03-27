# coding:utf-8
import os
import smtplib
import time
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import utils.HTMLTestRunner
# ###下面三行代码python2报告出现乱码时候可以加上####
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 这个是优化版执行所有用例并发送报告，分四个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）
def add_case(case_path, rule):
    '''加载所有的测试用例'''
    testunit = unittest.TestSuite()
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    #     for testcase in test_suite:
    #         testunit.addTests(testcase)
    #         print testunit
    testunit.addTests(discover)
    # 直接加载discover
    # print(testunit)
    return testunit

def run_case(all_case, report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    # 报告名字带日期时间
    report_abspath = os.path.join(report_path, now + "result.html")
    # report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    runner = utils.HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                 title=u'自动化测试报告,测试结果如下：',
                                                 description=u'用例执行情况：')
    # 调用add_case函数返回值

    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file

def send_mail(sender, psw, receiver, smtpserver, report_file):
    '''发送最新的测试报告内容'''
    # 读取测试报告的内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
        # 定义邮件内容
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = u"自动化测试报告"
        msg["from"] = sender
        msg["to"] = psw
        # 加上时间戳
        msg["date"] = time.strftime('%a, %d %b %Y %H_%M_%S %z')
        msg.attach(body)
        # 添加附件
        att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        msg.attach(att)
        # 登录邮箱
        smtp = smtplib.SMTP()
        # 连接邮箱服务器
        smtp.connect(smtpserver)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('3 report email has send out !')

if __name__ == "__main__":
    # 测试用例的路径、匹配规则
    case_path = r"e:\PycharmProjects\test_RWWY\testcase\web"
    rule = "Case*.py"

    # 1加载用例
    all_case = add_case(case_path, rule)
    # 生成测试报告的路径
    report_path = r"e:\PycharmProjects\test_RWWY\report"
    # 2执行用例
    run_case(all_case, report_path)

    # 3获取最新的测试报告
    report_file = get_report_file(report_path)

    # 邮箱配置
    # ----------1.跟发件相关的参数------
    smtpserver = "smtp.126.com"             # 发件服务器
    port = 0                                # 端口
    sender = "uuyaly@126.com"                 # 账号
    psw = "612101010"                  # 密码
    receiver = ["uuuyaly@qq.com", "oscaryou@qq.com"]           # 接收人
    subject = "自动化测试报告"
    # body = '<p>这个是自动发送的邮件</p>'     # 定义邮件正文为html格式

    # ----------2.编辑邮件的内容------
    # 读文件
    with open(report_file, "rb")as fp:
        mail_body = fp.read()
        msg = MIMEMultipart()
        msg['from'] = sender
        msg['to'] = ";".join(receiver)      # 多收件人list转str
        msg['subject'] = subject
        # 正文
        body = MIMEText(mail_body, "html", "utf-8")
        msg.attach(body)
        # 附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment;filename="report.html"'
        msg.attach(att)
    # ----------3.发送邮件------
    # 为了兼容qq邮箱的SSL
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)                # 连服务器
        smtp.login(sender, psw)                 # 登录
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)                 # 登录

    # smtp.sendmail(sender, receiver, msg.as_string())    # 发送
    # smtp.quit()                             # 关闭
    # 授权码 qq（uuu）邮箱密码 kjhpjigpcglmbgde