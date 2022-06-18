#-*-coding: utf-8-*-
#@Time  :2022/3/6 5:31
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: Python_mailV2.py


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#邮件主题
subject='Python send email test'

#发送的附件
with open('log.txt','rb') as f:
    send_att = f.read()

att = MIMEText(send_att, 'text','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="log.txt"'

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = "sender@sina.com"
msg.attach(att)

#发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.sina.com")
smtp.login("sender@sina.com", "test")
smtp.sendmail("sender@sina.com", "receiver@qq.com", msg.as_string())
smtp.quit()
