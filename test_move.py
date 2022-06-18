#-*-coding: utf-8-*-
#@Time  :2021/8/8 9:26
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_move.py

from selenium import webdriver

driver = webdriver.Chrome()
#访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

#访问新闻页
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to %s " %(first_url))
driver.back()

#手动刷新
driver.refresh()

#前进到新闻页
print("forward to %s " %(second_url))
driver.forward()

driver.quit()