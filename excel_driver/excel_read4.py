#-*-coding: utf-8-*-
#@Time  :2022/1/3 11:26
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: excel_read4.py

'''
读取Excel测试用例的数据内容，并用于自动化测试执行
'''

#获取sheet页内容
import openpyxl

from web_keys.keys_plus5 import Key

excel = openpyxl.load_workbook('../data/demo.xlsx')
# sheet = excel['Sheet1']
for name in excel.sheetnames:
    sheet =excel[name]
    print("********{}********".format(name))
    for values in sheet.values:
        # print(values)
        #用例正文一定是有编号的，可以基于编号来判定是否读取到用例正文内容
        if type(values[0]) is int:
            print("正在执行操作步骤{}:{}".format(values[1],values[5]))
            # print(values)
            #操作步骤关联参数的管理
            data = {}
            data['name'] = values[2]
            data['value'] = values[3]
            data['txt'] = values[4]
            #将为None的参数进行清理
            for k in list(data.keys()):
                if data[k] is None:
                    del data[k]
            # print(data)
            #管理操作行为，并将参数进行传入
            #1.实例化key对象
            if values[1]=='open_browser':
                key =Key(**data) #key=Key(txt='Chrome')
            #2.基于Key对象执行的操作行为
            else:
                getattr(key,values[1])(**data)