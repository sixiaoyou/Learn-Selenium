#-*-coding: utf-8-*-
#@Time  :2021/8/8 9:42
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_submit.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search_text=driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()

driver.quit()