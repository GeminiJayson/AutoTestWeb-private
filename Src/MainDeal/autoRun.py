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
import time
import Src.PreDeal.casePreDeal as CPD
from Src.BasicRef.process_log import Logger
from Src.BasicRef.process_log_toConsle import ToConsleLogger
from Src.TCexecution.runTestCase import runTestCase


def autoRun():
    log = Logger(level="debug").logger
    toConsleLog = ToConsleLogger(level="debug").logger
    toFileLog = Logger(level="debug")
    # 循环开始
    casedealinfoDics = CPD.getAllCaseDeal().casedealinfoDic
    nrow = len(casedealinfoDics)
    toConsleLog.info('There are have %d cases needed to execute' % nrow)
    for casedealinfoDic in casedealinfoDics:
        log.info('\n========================' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
            time.time())) + '========================')
        log.info(casedealinfoDic)
        runTestCase().switchRun(casedealinfoDic)


if __name__ == '__main__':
    autoRun()
