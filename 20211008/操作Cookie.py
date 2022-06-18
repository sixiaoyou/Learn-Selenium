#-*-coding: utf-8-*-
#@Time  :2021/10/9 6:34
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 操作Cookie.py
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#获得所有Cookie信息并打印
cookie = driver.get_cookies()
print(cookie)

#添加Cookie信息
driver.add_cookie({'name': 'key-aaaaaaaa','value': 'value-bbbbbbb'})

#遍历指定的Cookies
for cookie in driver.get_cookies():
    print("%s -> %s" %(cookie['name'],cookie['value']))

