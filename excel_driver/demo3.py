#-*-coding: utf-8-*-
#@Time  :2022/1/3 11:00
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: demo3.py

'''
    Excel文件操作的demo实例
        通过Excel文件管理测试数据
        1.读取Excel文件
            获取Excel文件
            获取对应的sheet页
            获取指定的单元格
        2.读取其中的测试数据
        3.基于数据来执行测试
'''
#获取excel
import openpyxl

#获取excel
excel = openpyxl.load_workbook('../data/demo.xlsx')

#指定sheet页
sheet =excel['Sheet1']

#获取单元格及内容
for values in sheet.values:
    print(values)