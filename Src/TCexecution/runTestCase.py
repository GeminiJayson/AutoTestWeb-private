import re
import re
import time

from dateutil.parser import parse
from selenium import webdriver

import Src.BasicRef.pathUtil as path
import Src.PreDeal.dataPreDeal as DPD
from Src.BasicRef.process_log import Logger


# 一定要和单元测试框架一起用

class runTestCase(object):
    log = Logger(level="debug").logger
    toFileLog = Logger(level="debug")
    module_path = path.pathutil().rootPath
    imagepath = ''
    datatypemenu = ['ElementsInfo', 'InputData', 'OutputData']
    browser = webdriver.Chrome()
    urlReg = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def __init__(self):
        self.switch = {
            "打开": lambda casedealinfoDic, ifrerun: self.test_open(casedealinfoDic, ifrerun),
            "点击": lambda casedealinfoDic, ifrerun: self.test_click(casedealinfoDic, ifrerun),
            "输入": lambda casedealinfoDic, ifrerun: self.test_input(casedealinfoDic, ifrerun),
            "清除": lambda casedealinfoDic, ifrerun: self.test_clear(casedealinfoDic, ifrerun),
            "等待": lambda casedealinfoDic, ifrerun: self.test_wait(casedealinfoDic, ifrerun),
            "断言": lambda casedealinfoDic, ifrerun: self.test_assertion(casedealinfoDic, ifrerun),
            "引入": lambda casedealinfoDic, ifrerun: self.test_introduce(casedealinfoDic, ifrerun),
            "最大化": lambda casedealinfoDic, ifrerun: self.test_maximize(casedealinfoDic, ifrerun)
        }

    # 定义一个保存截图函数
    def save_img(self, img_name):
        self.imagepath = self.module_path + '/Output/Resources/' + img_name + '.png'
        self.browser.get_screenshot_as_file(self.imagepath)

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self, url):
        self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.browser.set_window_size(1920, 1080)
        print("开始测试时间：", self.starttime)
        self.browser.get(url)
        #time.sleep(3)

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        #time.sleep(3)
        self.browser.quit()
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间：", self.endtime)
        totaltime = (self.endtime - self.starttime).total_seconds()
        print("总时长：", totaltime, "秒")

    def switchRun(self, casedealinfoDic):
        ifrerun = False
        if casedealinfoDic[1][0] is not None:
            if self.urlReg.match(DPD.getAllData().checkIfExists(self.datatypemenu[1], casedealinfoDic[1][0])):
                ifrerun = True
        try:
            self.switch[casedealinfoDic[1][2]](casedealinfoDic, ifrerun)
        except KeyError as e:
            self.log(e)

    def test_open(self, casedealinfoDic, ifrerun):
        if ifrerun == True:
            self.setUp(DPD.getAllData().checkIfExists(self.datatypemenu[1], casedealinfoDic[1][0]))
            self.save_img(casedealinfoDic[0])
        self.tearDown()

    def test_click(self, casedealinfoDic, ifrerun):
        pass

    def test_input(self, casedealinfoDic, ifrerun):
        pass

    def test_clear(self, casedealinfoDic, ifrerun):
        pass

    def test_wait(self, casedealinfoDic, ifrerun):
        pass

    def test_assertion(self, casedealinfoDic, ifrerun):
        pass

    def test_introduce(self, casedealinfoDic, ifrerun):
        pass

    def test_maximize(self, casedealinfoDic, ifrerun):
        pass


if __name__ == '__main__':
    t = runTestCase()
    t.switchRun(["iRE_Site1", "NA", "打开", "提示", "errorMessage", "LoginWarning1"])
