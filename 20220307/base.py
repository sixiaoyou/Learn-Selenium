#-*-coding: utf-8-*-
#@Time  :2022/3/7 5:33
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: base.py

import time

class BasePage:
    """
    基础page层,封装一些常用方法
    """
    def __init__(self,driver):
        self.driver = driver

    #打开页面
    def open(self,url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    #id定位
    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    #获取title
    def get_title(self):
        return self.driver.title