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

from Src.BasicRef.process_log import Logger
from Src.TCexecution.casesuite import Case
from Src.Packages.HTMLTestRunner import HTMLTestRunner
import unittest
from Src.BasicRef.pathUtil import pathutil
import time


def autoRun():
    reportname = pathutil().rootPath + "/Output/Report/Test Report_Build" + time.strftime('%Y%m%d', time.localtime(
        time.time())) + ".html"
    log = Logger(level="debug").logger
    log.info('\n========================' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
        time.time())) + '========================')
    tset_suite = unittest.TestLoader().loadTestsFromTestCase(Case)
    with open(reportname, "wb") as report:
        runner = HTMLTestRunner(stream=report, title=u"测试报告", description=u"用例测试情况")
        runner.run(tset_suite)


if __name__ == '__main__':
    autoRun()
