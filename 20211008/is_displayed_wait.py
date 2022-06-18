#-*-coding: utf-8-*-
#@Time  :2021/10/8 5:53
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: is_displayed_wait.py
from time import sleep,ctime
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

print(ctime())

for i in range(10):
    try:
        el=driver.find_element_by_id("kw22")
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
print(ctime())

driver.quit()