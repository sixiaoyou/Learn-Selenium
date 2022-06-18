#-*-coding: utf-8-*-
#@Time  :2022/3/3 6:29
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: run_testsV2.py
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

#定义测试用例的目录为当前目录中的test_case/目录
test_dir ='../20211220'
suits=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=="__main__":
    #生成HTML格式的报告
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open('./test_report/'+now_time+'result.html','wb')
    runner = HTMLTestRunner(stream=fp,title="百度搜索测试报告",description="运行环境：windows10，Chrome浏览器")
    runner.run(suits)
    fp.close()