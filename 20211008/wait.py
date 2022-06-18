#-*-coding: utf-8-*-
#@Time  :2021/10/8 5:22
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: wait.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element = WebDriverWait(driver,5,0.5).until(
    EC.visibility_of_element_located((By.ID,"kw"))
)
element.send_keys('selenium')
driver.quit()
