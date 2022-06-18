#-*-coding: utf-8-*-
#@Time  :2021/12/20 6:27
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 窗口截图.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#截取当前窗口，指定截图图片的保存位置
driver.save_screenshot("./baidu_img.png")