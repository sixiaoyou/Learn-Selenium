#-*-coding: utf-8-*-
#@Time  :2021/8/28 15:06
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_send_keys.py

from selenium import webdriver
#调用key模块
from selenium.webdriver.common.keys import Keys

#在输入框输入内容
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#删除多输入的一个m
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#输入空格键+"教程"
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

#输入组合键Ctrl+a,全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

#输入组合键Ctrl+x,剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

#输入组合键Ctrl+v,粘贴输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

#用回车键代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTERN)
driver.quit()


