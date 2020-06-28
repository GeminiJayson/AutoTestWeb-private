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

from Src.BasicRef.process_log import Logger as log
from Src.BasicRef.pyse import Pyse
import Src.BasicRef.pathUtil as path
from Src.PreDeal.dataPreDeal import getAllData as GAD

class Action:
    def __init__(self):
        self.driver = Pyse("chrome")
        self.datatypemenu = ["ElementsInfo", "InputData", "OutputData"]

    def pre_do(self,data):
        return self.do_action(data)

    def do_action(self, data):
        try:

            Positioning_type = GAD().checkIfExists(self.datatypemenu[0], data["操作元素"])[0].split("By.")
            Positioning_value = GAD().checkIfExists(self.datatypemenu[0], data["操作元素"])[1]
            input_data = GAD().checkIfExists(self.datatypemenu[1], data["输入数据"])
            if data["操作类型"] == "断言":
                text = self.driver.get_element(Positioning_type + '=>' + Positioning_value).text
                return text
            if data["操作类型"] == "打开":
                self.driver.open(input_data)
            if data["操作类型"] == "点击":
                self.driver.click(Positioning_type + '=>' + Positioning_value)
            if data["操作类型"] == "清除":
                self.driver.clear(Positioning_type + '=>' + Positioning_value)
            # if data["动作"] == "等待":
            #     self.driver.wait(int(data["输入值"]))
            if data["操作类型"] == "输入":
                self.driver.type(Positioning_type + '=>' + Positioning_value, input_data)
            if data["操作类型"] == "滚动条下拉":
                self.driver.js( "var q=document.body.scrollTop=" + input_data + ";")
            if data["操作类型"] == "等待元素":
                self.driver.element_wait(Positioning_type + '=>' + Positioning_value, 10)
            if data["操作类型"] == "最大化":
                self.driver.max_window()
            if data["操作类型"] == "关闭浏览器":
                self.driver.close()
        except Exception as e :
            log().error("异常截图-"+data["操作类型"]+str(e))
            self.driver.save_png(path.pathutil().rootPath + '/Output/Resources/'+data['用例编号']+'.jpg')


