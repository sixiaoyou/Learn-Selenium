#-*-coding: utf-8-*-
#@Time  :2021/8/8 9:21
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_size.py
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.baidu.com")

#参数数字为像素
print("设置浏览器宽480、高800显示")
# driver.set_window_size(480,800)
driver.maximize_window()
driver.quit()