#-*-coding: utf-8-*-
#@Time  :2021/10/9 5:55
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 下拉框处理.py

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

#打开搜索设置
link = driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text("搜索设置").click()

#搜索结果显示条数
sel=driver.find_element_by_xpath("//select[@id='nr']")

#value="20"
Select(sel).select_by_value('20')
sleep(2)

#<option>每页显示50条</option>
Select(sel).select_by_visible_text("每页显示50条")
sleep(2)

#根据下拉选项的索引进行选择
Select(sel).select_by_index(0)
sleep(2)

driver.quit()
