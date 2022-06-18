#-*-coding: utf-8-*-
#@Time  :2022/3/5 6:06
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: python_mail.py

import smtplib
from email.mime.text import MIMEText
from email.header import Header

subject = 'Python email test'

#编写HTML类型的邮件正文
msg = MIMEText('你好', 'text','utf-8')
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = Header("sender@sina.com")
msg['To'] = Header("receiver@qq.com")

#发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.sina.com")
smtp.login("sender@sina.com", "test")
smtp.sendmail("sender@sina.com", "receiver@qq.com", msg.as_string())
smtp.quit()


