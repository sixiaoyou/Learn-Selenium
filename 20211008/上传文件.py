#-*-coding: utf-8-*-
#@Time  :2021/10/9 6:16
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 上传文件.py

import os
from selenium import webdriver

file_path = os.path.abspath('./files/')

driver = webdriver.Chrome()
upload_page = 'file:///'+file_path+'upfile.html'
driver.get(upload_page)

#定位上传按钮，添加本地文件
driver.find_element_by_id("file").send_keys(file_path + 'test.txt')