#-*-coding: utf-8-*-
#@Time  :2021/12/25 7:05
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_baiduV3.py
import unittest
from time import sleep
from selenium import webdriver

class TestBaiduV3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "http://www.baidu.com"

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)

    def test_search_key_selenium(self):
        search_key = "selenium"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    def test_search_key_unittest(self):
        search_key = "unittest"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
