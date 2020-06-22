#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pathUtil.py    
@Contact :   geminijayson@gmail.com
@Functional description:


     @Modify Time   |    @Author   |@Version    
--------------------|--------------|--------    
2020/5/27 0027-19:02| GeminiJayson | V0.0.1        
"""
import sys
import os


class pathutil(object):
    """路径处理工具类"""

    def __init__(self):
        # 判断调试模式
        debug_vars = dict((a, b) for a, b in os.environ.items()
                          if a.find('IPYTHONENABLE') >= 0)
        # 根据不同场景获取根目录
        if len(debug_vars) > 0:
            """当前为debug运行时"""
            self.rootPath = sys.path[2]
        elif getattr(sys, 'frozen', False):
            """当前为exe运行时"""
            self.rootPath = os.getcwd()
        else:
            """正常执行"""
            self.rootPath = sys.path[1]
        # 替换斜杠
        self.rootPath = self.rootPath.replace("\\", "/")

        # 被调函数名称
        self.funcName = sys._getframe().f_code.co_name
        # 被调函数所在行号
        self.funcNo = sys._getframe().f_back.f_lineno

        # 被调函数所在文件名称
        self.funcFile = sys._getframe().f_code.co_filename

    def getPathFromResources(self, fileName):
        """按照文件名拼接资源文件路径"""
        filePath = "%s/resources/%s" % (self.rootPath, fileName)
        return filePath


if __name__ == '__main__':
  """测试"""
  PathUtil = pathutil()
  # path = PathUtil.getPathFromResources("context.ini")
  print(PathUtil.rootPath)