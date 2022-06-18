#-*-coding: utf-8-*-
#@Time  :2021/8/8 10:05
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_ActionChains.py
from selenium import webdriver

#引入ActionChains类
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")
driver.maximize_window()

#定位到要悬停的元素
above=driver.find_element_by_link_text("设置")
#对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

#....