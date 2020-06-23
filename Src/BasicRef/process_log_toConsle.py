#!F:\CASCO-WorkSpace\CCTest\AutoRunTool_modify
# -*- coding: utf-8 -*-
# @Time :  下午 03:15
# @Author : GeminiJayson
# @Site : 
# @File : process_log_toConsle.py
# @Software : PyCharm

import logging
# 日志输出
# 日志输出
import time
import Src.BasicRef.pathUtil as path


class ToConsleLogger(object):
    # 定义常量
    module_path = path.pathutil().rootPath
    logpath = module_path + '\\Output\\Log\\RunLog' + time.strftime('%Y%m%d', time.localtime(
        time.time())) + '.log'
    # 日志级别关系映射
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }
    streamHandler = logging.StreamHandler()

    def __init__(self, filename=logpath, level="info", fmt="%(message)s"):
        format_str = logging.Formatter(fmt)
        self.logger = logging.getLogger(filename)
        # 设置日志输出文件
        self.streamHandler.setFormatter(format_str)
        self.logger.addHandler(self.streamHandler)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))

    def debug(self, message):
        self.fontColor('\033[32m%s\033[0m')
        self.logger.debug(message)

    def info(self, message):
        self.fontColor('\033[34m%s\033[0m')
        self.logger.info(message)

    def warning(self, message):
        self.fontColor('\033[37m%s\033[0m')
        self.logger.warning(message)

    def error(self, message):
        self.fontColor('\033[31m%s\033[0m')
        self.logger.error(message)

    def critical(self, message):
        self.fontColor('\033[35m%s\033[0m')
        self.logger.critical(message)

    def fontColor(self, color):
        # 不同的日志输出不同的颜色
        formatter = logging.Formatter(color % '%(message)s')
        self.streamHandler.setFormatter(formatter)
        self.logger.addHandler(self.streamHandler)
