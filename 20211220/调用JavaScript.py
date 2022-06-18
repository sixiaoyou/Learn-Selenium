#-*-coding: utf-8-*-
#@Time  :2021/12/20 5:41
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 调用JavaScript.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(800,600)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

#通过JavaScript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450);"
driver.execute_script(js)
