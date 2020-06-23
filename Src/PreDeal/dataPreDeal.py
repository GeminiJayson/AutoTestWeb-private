#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   dataPreDeal.py
@Contact :   geminijayson@gmail.com
@Functional description:


     @Modify Time   |    @Author   |@Version
--------------------|--------------|--------
2020/5/26 0026-20:28| GeminiJayson | V0.0.1
"""
import Src.BasicRef.process_ExcelDeal as ExcelDeal


class getAllData(object):
    def __init__(self):
        self.config_excel_path = '\\Config\\testCFG.xls'
        self.datacfg_sheetname = u'DataConfig'
        self.elementsinfo_sheetname = u'ElementsInfo'
        self.inputdata_sheetname = u'InputData'
        self.outputdata_sheetname = u'OutputData'
        self.initelementsinfoDic = []
        self.initinputdataDic = []
        self.initoutputdataDic = []
        self.elementsinfoDic = {}
        self.inputdataDic = {}
        self.outputdataDic = {}
        self.readalldata()

    def readalldata(self):
        self.initelementsinfoDic = ExcelDeal.merge_cell(self.elementsinfo_sheetname)
        self.initinputdataDic = ExcelDeal.merge_cell(self.inputdata_sheetname)
        self.initoutputdataDic = ExcelDeal.merge_cell(self.outputdata_sheetname)
        #处理列表类数据，特点：单标识符对应多组数据
        index = 0
        inputdatesameDic = {}
        while index < len(self.initinputdataDic):
            samelist = []
            samevalue = []
            samelist.append(index)
            for index1 in range(index + 1, len(self.initinputdataDic)):
                if self.initinputdataDic[index]["标识符"] == self.initinputdataDic[index1]["标识符"]:
                    samelist.append(index1)

            if len(samelist) != 1:
                for same in samelist:
                    samevalue.append(self.initinputdataDic[same]["输入数据"])
                inputdatesameDic.update({self.initinputdataDic[samelist[-1]]["标识符"]: samevalue})
            index = samelist[-1] + 1
        index = 0
        elementssameDic = {}
        while index < len(self.initelementsinfoDic):
            samelist = []
            samevalue = []
            samelist.append(index)
            for index1 in range(index + 1, len(self.initelementsinfoDic)):
                if self.initelementsinfoDic[index]["变量名称"] == self.initelementsinfoDic[index1]["变量名称"]:
                    samelist.append(index1)

            if len(samelist) != 1:
                for same in samelist:
                    samevalue.append([self.initelementsinfoDic[same]["定位方式"], self.initelementsinfoDic[same]["元素"]])
                elementssameDic.update({self.initelementsinfoDic[samelist[-1]]["变量名称"]: samevalue})
            index = samelist[-1] + 1
        index = 0
        outputdatasameDic = {}
        while index < len(self.initoutputdataDic):
            samelist = []
            samevalue = []
            samelist.append(index)
            for index1 in range(index + 1, len(self.initoutputdataDic)):
                if self.initoutputdataDic[index]["标识符"] == self.initoutputdataDic[index1]["标识符"]:
                    samelist.append(index1)

            if len(samelist) != 1:
                for same in samelist:
                    samevalue.append(self.initoutputdataDic[same]["输出数据"])
                outputdatasameDic.update({self.initoutputdataDic[samelist[-1]]["标识符"]: samevalue})
            index = samelist[-1] + 1

        for index in range(len(self.initelementsinfoDic)):
            self.elementsinfoDic.update({self.initelementsinfoDic[index]["变量名称"]: [
                self.initelementsinfoDic[index]["定位方式"],
                self.initelementsinfoDic[index]["元素"]]})
        self.elementsinfoDic.update(elementssameDic)

        for index in range(len(self.initinputdataDic)):
            self.inputdataDic.update({self.initinputdataDic[index]["标识符"]:
                                          self.initinputdataDic[index]["输入数据"]})
        self.inputdataDic.update(inputdatesameDic)

        for index in range(len(self.initoutputdataDic)):
            self.outputdataDic.update({self.initoutputdataDic[index]["标识符"]:
                self.initoutputdataDic[index]["输出数据"]})
        self.outputdataDic.update(outputdatasameDic)

    def checkIfExists(self, datatype, keyword):
        if datatype == "ElementsInfo":
            if keyword in self.elementsinfoDic:
                return self.elementsinfoDic[keyword]
            else:
                raise Exception("要操作的元素不存在于配置表中，请检查！")
        if datatype == "InputData":
            if keyword in self.inputdataDic:
                return self.inputdataDic[keyword]
            else:
                raise Exception("需求的输入数据不存在于配置表中，请检查！")
        if datatype == "OutputData":
            if keyword in self.outputdataDic:
                return self.outputdataDic[keyword]
            else:
                raise Exception("需求的输出数据不存在于配置表中，请检查！")


if __name__ == '__main__':
    t = getAllData()
    print(t.checkIfExists("InputData", "loginBtnEle"))
