#-*-coding: utf-8-*-
#@Time  :2021/8/8 9:47
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_text.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


#获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

#返回百度页面底部备案信息
text=driver.find_element_by_id("bottom_layer").text
print(text)

#返回元素的属性值,可以是id、name、type或其他任意属性
attribute=driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

#返回元素的结果是否可见，返回结果为True或False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()