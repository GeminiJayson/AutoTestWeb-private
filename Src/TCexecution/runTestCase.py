import os
import time



from Src.BasicRef.process_log_toConsle import ToConsleLogger
from Src.BasicRef.process_log import Logger
import unittest
from selenium import webdriver
from dateutil.parser import parse
from BeautifulReport import BeautifulReport
import Src.PreDeal.dataPreDeal as DPD
import Src.BasicRef.pathUtil as path

class runTestCase(object):
    log = Logger(level="debug").logger
    toConsleLog = ToConsleLogger(level="debug").logger
    toFileLog = Logger(level="debug")
    module_path = path.pathutil().rootPath
    imagepath = ''
    def __init__(self):

        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.browser = webdriver.Chrome()
        self.switch = {
            "打开": lambda casedealinfoDic: self.test_open(casedealinfoDic),
            "点击": lambda casedealinfoDic: self.test_click(casedealinfoDic),
            "输入": lambda casedealinfoDic: self.test_input(casedealinfoDic),
            "清除": lambda casedealinfoDic: self.test_clear(casedealinfoDic),
            "等待": lambda casedealinfoDic: self.test_wait(casedealinfoDic),
            "断言": lambda casedealinfoDic: self.test_assertion(casedealinfoDic),
            "引入": lambda casedealinfoDic: self.test_introduce(casedealinfoDic),
            "最大化": lambda casedealinfoDic: self.test_maximize(casedealinfoDic)
        }

    # 定义一个保存截图函数
    def save_img(self, img_name):
        self.imagepath = self.module_path + "\\Output\\Resource\\" +  img_name + ".png"
        self.browser.get_screenshot_as_file(self.imagepath)

    # 启动函数，每个用例测试前，都会执行该函数
    def setUp(self, url):
        self.browser.set_window_size(1920, 1080)
        print("开始测试时间：", self.starttime)
        self.browser.get(url)
        time.sleep(3)

    # 结束函数，每个用例测试结束后，都会执行该函数
    def tearDown(self):
        time.sleep(3)
        self.browser.quit()
        print("测试结束时间：", self.endtime)
        totaltime = (self.endtime - self.starttime).total_seconds()
        print("总时长：", totaltime, "秒")

    def switchRun(self, casedealinfoDic):
        try:
            self.switch[casedealinfoDic[2]](casedealinfoDic)
        except KeyError as e:
            self.toConsleLog(e)

    @BeautifulReport.add_test_img(imagepath)
    def test_open(self, casedealinfoDic):
        self.setUp(DPD.getAllData().inputdataDic[casedealinfoDic[0]])
        self.save_img('打开网页')
        self.tearDown()

    def test_click(self, casedealinfoDic):
        pass

    def test_input(self, casedealinfoDic):
        pass

    def test_clear(self, casedealinfoDic):
        pass

    def test_wait(self, casedealinfoDic):
        pass

    def test_assertion(self, casedealinfoDic):
        pass

    def test_introduce(self, casedealinfoDic):
        pass

    def test_maximize(self, casedealinfoDic):
        pass


if __name__ == '__main__':
    t = runTestCase()
    t.switchRun(["iRE_Site1", "NA", "打开", "提示", "errorMessage", "LoginWarning1"])
