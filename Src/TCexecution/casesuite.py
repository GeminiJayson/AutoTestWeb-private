#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   autoRun.py
@Contact :   geminijayson@gmail.com
@Functional description:


     @Modify Time   |    @Author   |@Version
--------------------|--------------|--------
2020/6/21 0021-23:56| GeminiJayson | V0.0.1
"""
import unittest
import time
import Src.BasicRef.ddtSelenium as ddtSelenium
from Src.PreDeal.casePreDeal import getAllCaseDeal as CPD
from Src.BasicRef.process_log import Logger as log
from Src.TCexecution.action import Action
import Src.BasicRef.pathUtil as path


@ddtSelenium.ddt
class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = Action()
        # cookies = eval(config.get_config("normal","cookie"))
        # cls.action.driver.driver.add_cookie(cookies)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.action.driver.close()

    @ddtSelenium.data(*CPD().readalldata())
    def testcase(self, data):
        text = ''
        log().info(str(data[list(data.keys())[0]]) + "-开始")
        if data["操作类型"] == "等待":
            time.sleep(int(data["输入数据"]))
        else:
            text = self.action.pre_do(data)

        if data["操作类型"] == "断言":
            log().info("断言："+ str(data[list(data.keys())[0]]))
            if text != data["输入数据"]:
                log().info("断言截图：" + str(data[list(data.keys())[0]]))
                self.action.driver.save_png(path.pathutil().rootPath + '/Output/Resources/'+data['用例编号']+'.jpg')
            self.assertEqual(text, data["输入数据"])
        log().info(str(data[list(data.keys())[0]]) + "-结束")
