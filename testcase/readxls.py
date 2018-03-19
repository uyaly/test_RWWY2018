filePath = "D:\\PycharmProjects\\3\\study\\lytest\\data.xlsx"
sheetName = "Sheet1"
data = ExcelUtil(filePath, sheetName)
testData = data.dict_data()
print testData
@ddt.ddt
class Bolg(unittest.TestCase):
    u'''登录博客'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
    def login(self, username, psw):
        u'''这里写了一个登录的方法,账号和密码参数化'''
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)
    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print text
            return True
        except:
            return False
    @ddt.data(*testData)
    def test_login(self, data):
        u'''登录案例参考'''
        print ("当前测试数据%s"%data)
        # 调用登录方法
        self.login(data["username"], data["password"])
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()