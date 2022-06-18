#-*-coding: utf-8-*-
#@Time  :2021/12/25 5:47
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: Selenium_Demo.py
from selenium import webdriver

#创建浏览器驱动，生成浏览器
driver = webdriver.Chrome()

#访问指定的url
driver.get("http://www.baidu.com")

#定位输入框元素，进行输入
el=driver.find_element('id',"kw")
# driver.find_element_by_id()
el.send_keys("虚竹")
#定位按钮，进行点击
driver.find_element("id","su").click()