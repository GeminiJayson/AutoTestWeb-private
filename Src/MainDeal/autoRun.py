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
import os
import time
import Src.BasicRef.pathUtil as PU
import Src.PreDeal.casePreDeal as CPD
import Src.PreDeal.dataPreDeal as DPD
from Src.BasicRef.process_log import Logger
import unittest
from selenium import webdriver
from dateutil.parser import parse
from BeautifulReport import BeautifulReport


def autoRun():
    log = Logger(level="debug").logger
    # 循环开始
    casedealinfoDics = CPD.getAllCaseDeal().casedealinfoDic
    nrow = len(casedealinfoDics)
    print('There are have %d cases needed to execute' % nrow)
    for casedealinfoDic in casedealinfoDics:
        log.debug('\n========================' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
            time.time())) + '========================')
        log.info(casedealinfoDic)


if __name__ == '__main__':
    autoRun()
