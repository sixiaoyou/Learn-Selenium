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

from web_keys.keys1 import Key

#获取单元格信息，处理参数
def new_data(value):
    if values[2] != None:
        data = {}
    #字符串内容的切割,先切割分号，区分多组不同参数
        str_temp=value.split(';')
        #切割等号，区分多组参数名与值的K-V对
        for temp in str_temp:
            temp = temp.split('=',1)
            data[temp[0]] = temp[1]
    else:
        data = None
    return data

excel = openpyxl.load_workbook('../data/demo_new.xlsx')
# sheet = excel['Sheet1']
for name in excel.sheetnames:
    sheet =excel[name]
    print("********{}********".format(name))
    for values in sheet.values:
        # print(values) 
        #用例正文一定是有编号的，可以基于编号来判定是否读取到用例正文内容
        if type(values[0]) is int:
            print("正在执行操作步骤{}:{}".format(values[1],values[3]))
            # print(values)

            #操作步骤关联参数的管理
            data = new_data(values[2])
            # print(data)
            #管理操作行为，并将参数进行传入
            #1.实例化key对象
            if values[1]=='open_browser':
                key =Key(**data) #key=Key(txt='Chrome')
            # 3.断言结果的Excel表格写入
            elif 'assert' in values[1]:
                status = getattr(key,values[1])(**data)
                #断言成功
                if status:
                    print('excel写入成功')
                #断言失败
                else:
                    print('excel写入失败')
            #2.基于Key对象执行的操作行为
            else:
                if data is not None:
                    getattr(key,values[1])(**data)
                else:
                    getattr(key,values[1])()
