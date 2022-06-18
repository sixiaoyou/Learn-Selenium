#-*-coding: utf-8-*-
#@Time  :2021/8/28 15:41
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_title.py

from time import sleep
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
print("Before search=====================")

#打印当前页面title
title=driver.title
print("title:"+title)

#打印当前页面URL
now_url=driver.current_url
print("URL:"+now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

print("After search========================")

#再次打印当前页面title
title=driver.title
print("title:"+title)

#再次打印当前页面URL
now_url=driver.current_url
print("URL:"+now_url)

#获取搜索结果条数
num = driver.find_element_by_class_name("nums").text
print("result:"+num)

driver.quit()