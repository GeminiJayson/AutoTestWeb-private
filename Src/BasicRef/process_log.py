import logging
from logging import handlers
# 日志输出
import time
import Src.BasicRef.pathUtil as path


class Logger(object):
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

    def __init__(self, filename=logpath, level="info", when="D", backupCount=3,
                 fmt="%(message)s"):
        # 设置日志输出格式
        format_str = logging.Formatter(fmt)
        # 设置日志输出文件
        self.logger = logging.getLogger(filename)
        if not self.logger.handlers:
            # 设置控制台中输出日志格式
            self.streamHandler.setFormatter(format_str)

            # 设置日志输出到文件（指定间隔时间自动生成文件的处理器  --按日生成）
            # filename：日志文件名，interval：时间间隔，when：间隔的时间单位， backupCount：备份文件个数，若超过这个数就会自动删除
            fileHandler = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backupCount,
                                                            encoding="utf-8")
            # 设置日志文件中的输出格式
            fileHandler.setFormatter(format_str)
            # 设置日志级别
            self.logger.setLevel(self.level_relations.get(level))
            self.logger.addHandler(fileHandler)
            self.logger.addHandler(self.streamHandler)

    def M_info(self, i_line, str_actualResult, str_examinedField, str_expected_value, str_actualValue, str_stepResult, str_scriptNote):
        self.logger.info('【' + str(i_line) + '】===>' + str_actualResult)
        self.logger.info(str_examinedField)
        self.logger.info(str_expected_value)
        self.logger.info(str_actualValue)
        self.logger.info(str_stepResult)
        self.logger.info('#script_note#' + str_scriptNote)

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
