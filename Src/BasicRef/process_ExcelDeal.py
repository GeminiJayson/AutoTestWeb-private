#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   process_ExcelDeal.py    
@Contact :   geminijayson@gmail.com
@Functional description:


     @Modify Time   |    @Author   |@Version    
--------------------|--------------|--------    
2020/5/26 0026-20:35| GeminiJayson | V0.0.1        
"""

import xlrd
import os
import xlutils
from xlutils.copy import copy
import Src.BasicRef.pathUtil as path

# 定义常量
module_path = path.pathutil().rootPath
config_excel_path = '/Config/testCFG.xls'


def setOutCell(outSheet, col, row, value):
    """

    :param outSheet:
    :param col:
    :param row:
    :param value:
    :func : Change cell value without changing formatting.
    :return:
    """

    def _getOutCell(outSheet, colIndex, rowIndex):
        """ HACK: Extract the internal xlwt cell representation. """
        row = outSheet._Worksheet__rows.get(rowIndex)
        if not row : return None

        cell = row._Row__cells.get(colIndex)
        return cell

    # HACK to retain cell style.
    previousCell = _getOutCell(outSheet, col, row)
    # END HACK, PART I

    outSheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx



def writeSingleExcel(operation_sheetname, row, col, writevalue):
    """
    Function:
        写单个值

    Args:
        operation_sheetname:
        row:
        col:
        writevalue:

    Returns:

    """
    excel_path = module_path + config_excel_path
    rb = xlrd.open_workbook(excel_path, formatting_info=True)  # rb打开该excel，formatting_info=True表示打开excel时并保存原有的格式
    wb = xlutils.copy.copy(rb)  # 创建一个可写入的副本
    newws = wb.get_sheet(operation_sheetname)
    setOutCell(newws, col, row, writevalue)
    wb.save(excel_path)


def writemultipleExcel(operation_sheetname, srow, rownum, scol, colnum, writevaluelist):
    """
    Function:
        连续写多个值（单元格连续）

    Args:
        colnum:
        rownum:
        srow:
        writevaluelist:
        scol:
        operation_sheetname:

    Returns:

    """
    excel_path = module_path + config_excel_path
    rb = xlrd.open_workbook(excel_path, formatting_info=True)  # rb打开该excel，formatting_info=True表示打开excel时并保存原有的格式
    wb = xlutils.copy.copy(rb)  # 创建一个可写入的副本
    newws = wb.get_sheet(operation_sheetname)
    for i in range(rownum):
        for j in range(colnum):
            setOutCell(newws, scol + j, srow + i, writevaluelist)
    wb.save(excel_path)


def readExcelCell(operation_sheetname, i_line, j_column):
    """
    Function:
        从excel中获取cell信息

    Args:
        operation_sheetname:
        i_line:
        j_column:

    Returns:
        cellValue:
    """
    excel_path = module_path + config_excel_path
    data = xlrd.open_workbook(excel_path, formatting_info=True)
    table = data.sheet_by_name(operation_sheetname)
    cellValue = table.cell(i_line, j_column).value
    return cellValue


def readExcelNrows(operation_sheetname):
    """
    Function:
        获取行数

    Args:
        operation_sheetname:

    Returns:
        table.nrows - 1：

    """
    excel_path: str = module_path + config_excel_path
    data = xlrd.open_workbook(excel_path, formatting_info=True)
    table = data.sheet_by_name(operation_sheetname)
    return table.nrows - 1


def readExcelNcols(operation_sheetname):
    """
        Function:
            获取列数

        Args:
            operation_sheetname:

        Returns:
            table.ncols - 1：

        """
    excel_path: str = module_path + config_excel_path
    data = xlrd.open_workbook(excel_path, formatting_info=True)
    table = data.sheet_by_name(operation_sheetname)
    return table.ncols - 1


def list_dic(list1, list2):
    """
    Function:
        two lists merge a dict,a list as key,other list as value
    Args:
        list1:
        list2:

    Returns:

    """

    dic = dict(map(lambda x,y:[x,y], list1,list2))
    return dic


def merge_cell(operation_sheetname):
    """
    Function:
            单元格数据读取（可处理合并单元格）

    Args:
        sheet_info:

    Returns:

    """
    excel_path = module_path + config_excel_path
    data = xlrd.open_workbook(excel_path, formatting_info=True)
    sheet_info = data.sheet_by_name(operation_sheetname)
    merge = {}
    apply_dic = []
    merge_cells = sheet_info.merged_cells
    first_line = []
    if len(merge_cells) != 0:
        if str(merge_cells[0]).split("(")[1].split(")")[0].split(", ")[0] == "0":
            first_line = sheet_info.row_values(1)
        else:
            first_line = sheet_info.row_values(0)
    else:
        first_line = sheet_info.row_values(0)
    for (rlow, rhigh, clow, chigh) in merge_cells:
        if rlow == 0:
            value_mg_cell = sheet_info.cell_value(rlow + 1, clow)
        else:
            value_mg_cell = sheet_info.cell_value(rlow, clow)
        if rhigh-rlow == 1:
            # Merge transverse cells
            if rlow == 0:
                for n in range(chigh-clow-1):
                    merge[(rlow + 1, clow+n+1)] = value_mg_cell
            else:
                for n in range(chigh-clow-1):
                    merge[(rlow, clow+n+1)] = value_mg_cell
        elif chigh-clow == 1:
            # Merge Vertical Cells
            for n in range(rhigh-rlow-1):
                merge[(rlow+n+1, clow)] = value_mg_cell
    for i in range(1, sheet_info.nrows):  # 开始为组成字典准备数据
        other_line = sheet_info.row_values(i)
        for key in merge.keys():
            if key[0] == i:
                other_line[key[1]] = merge[key]
        # print(other_line)
        dic = list_dic(first_line, other_line)  # 调用组合字典的函数，传入key和value，字典生成
        apply_dic.append(dic)
    return apply_dic



if __name__ == '__main__':
    merge_cell('InputData')