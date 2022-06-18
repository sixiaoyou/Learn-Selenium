#-*-coding: utf-8-*-
#@Time  :2021/8/8 9:36
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_click.py

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

driver.quit()

