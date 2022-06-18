#-*-coding: utf-8-*-
#@Time  :2022/3/6 5:54
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: python_yagmail.py

import yagmail

#连接邮箱服务器
yag = yagmail.SMTP(user="sender@sina.com",password="test",host = "smtp.sina.com")

#邮件正文
subject = "主题，自动化测试报告"
contents = ['Hello','World']

#发送邮件
yag.send('receiver.com',subject,contents)