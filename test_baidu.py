#-*-coding: utf-8-*-
#@Time  :2021/7/21 6:49
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_baidu.py
#-*-coding: utf-8-*-
#@Time  :2021/7/21 6:02
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_baidu.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


driver.find_element_by_id("kw").send_keys("Learn-Selenium")
driver.find_element_by_id("su").click()
driver.quit()
