#-*-coding: utf-8-*-
#@Time  :2022/3/6 6:05
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: run_testsV3.py

import time
import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner

#把测试报告作为附件发送到指定邮箱
def send_mail(report):
    yag = yagmail.SMTP(user="sender@sina.com",password="test",host='smtp.sina.com')
    subject = "主题，自动化测试报告"
    contents = "正文，请查看附件"
    yag.send('receiveruu@qq.com',subject,contents,report)
    print('email has send out !')

if __name__ == '__main__':
    #定义测试用例的目录为当前目录
    test_dir ='.'
    suit = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

    #获取当前日期和时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    html_report='./test_report'+now_time+'result.html'
    fp = open(html_report,'wb')

    #调用HTMLTestRunner,运行测试用例
    runner = HTMLTestRunner(stream=fp,title="百度搜索测试报告",description="运行环境:windows10,Chrome浏览器")
    runner.run(suit)
    fp.close()
    send_mail(html_report)