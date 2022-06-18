#-*-coding: utf-8-*-
#@Time  :2022/1/2 10:03
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: keys1.py
from time import sleep

from selenium import webdriver

#不同的浏览器生成
def open_browser(type_):
    # if type_== 'chrome':
    #     driver = webdriver.Chrome()
    # elif type_ == 'firefox':
    #     driver = webdriver.Firefox()
    #基于反射机制，进行逻辑代码的简化
    try:
        driver = getattr(webdriver,type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    #临时driver对象
    # driver = webdriver.Chrome()
    #构造函数 基于不同的需求，创建不同的浏览器对象
    def __init__(self,type_):
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(10)

    #访问url
    def open(self,url):
        self.driver.get(url)

    #元素定位 一定要满足八种不同的元素定位方法
    def locate(self,name,value):
        return self.driver.find_element(name,value)

    #输入
    def input(self,name,value,txt):
        self.locate(name,value).send_keys(txt)

    #点击
    def click(self,name,value):
        self.locate(name,value).click()

    #强制等待
    def sleep(self,time_):
        sleep(int(time_))

    #关闭
    def quit(self):
        self.driver.quit()

    #断言
    def assert_txt(self,name,value,expect):
        try:
            reality= self.locate(name,value).text
            assert reality == expect,'{}不等于{}'.format(reality,expect)
            # print('断言成功')
            return True
        except Exception as e:
            # print(e)
            return False