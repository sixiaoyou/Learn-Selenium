#-*-coding: utf-8-*-
#@Time  :2021/10/8 6:46
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 警告框处理.py

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

#打开搜索设置
link=driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()

#获取警告框
alert = driver.switch_to.alert

#获取警告框提示信息
alert_text=alert.text
print(alert_text)

#接取警告框
alert.accept()
driver.quit()