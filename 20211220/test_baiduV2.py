#-*-coding: utf-8-*-
#@Time  :2021/12/25 6:44
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_baiduV2.py
import unittest
from time import sleep
from selenium import webdriver

class TestBaiduV2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.baidu.com"

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

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
