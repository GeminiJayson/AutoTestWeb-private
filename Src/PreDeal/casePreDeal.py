#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   casePreDeal.py
@Contact :   geminijayson@gmail.com
@Functional description:


     @Modify Time   |    @Author   |@Version
--------------------|--------------|--------
2020/5/26 0026-20:29| GeminiJayson | V0.0.1
"""
import Src.BasicRef.process_ExcelDeal as ExcelDeal


class getAllCaseDeal(object):
    def __init__(self):
        self.config_excel_path = '\\Config\\testCFG.xls'
        self.casecfg_sheetname = u'CaseConfig'

        self.initcasedealinfoDic = []
        self.casedealinfoDic = {}
        self.readalldata()

    def readalldata(self):
        popindex = 0
        self.initcasedealinfoDic = ExcelDeal.merge_cell(self.casecfg_sheetname)

        while popindex < len(self.initcasedealinfoDic):
            if self.initcasedealinfoDic[popindex]["用例编号"] == "用例编号" or self.initcasedealinfoDic[popindex]["用例编号"] == "":
                self.initcasedealinfoDic.pop(popindex)
                popindex = popindex
            else:
                popindex = popindex + 1
        #     self.casedealinfoDic.update(
        #         {self.initcasedealinfoDic[index]["用例编号"] + "-" + str(self.initcasedealinfoDic[index]["步骤号"]): [
        #             self.initcasedealinfoDic[index]["输入数据"],
        #             self.initcasedealinfoDic[index]["操作元素"],
        #             self.initcasedealinfoDic[index]["操作类型"],
        #             self.initcasedealinfoDic[index]["预期结果类型"],
        #             self.initcasedealinfoDic[index]["预期结果元素"],
        #             self.initcasedealinfoDic[index]["结果数据"], self.initcasedealinfoDic[index]["简短描述"]]})
        # self.casedealinfoDic.pop("用例编号-步骤号")
        # self.casedealinfoDic.pop("-")
        return self.initcasedealinfoDic

if __name__ == '__main__':
    t = getAllCaseDeal()
    print(t.casedealinfoDic)
