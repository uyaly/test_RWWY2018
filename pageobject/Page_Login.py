# coding:utf-8
from utils.ly_selenium import ly  # 导入4.11二次封装的类


class Page_Login(ly):
    # 定位器，定位页面元素
    username_loc = ("class name", 'userName')  # 输入账号
    password_loc = ("class name", 'passWord')
    submit_loc = ("class name", 'login_btn')
    title_loc = ("class name", 'login_title')

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        '''输入密码框'''
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        '''登录按钮'''
        self.click(self.submit_loc)

    def login(self, username, password):
        '''登录方法'''
        self.input_username(username)
        self.input_password(password)
        self.click_submit()