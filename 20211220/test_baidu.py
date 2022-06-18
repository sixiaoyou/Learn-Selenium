#-*-coding: utf-8-*-
#@Time  :2021/12/25 6:32
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_baidu.py
import unittest
from time import sleep
from selenium import webdriver

class TestBaidu(unittest.TestCase):
    """ 百度搜索测试 """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.baidu.com"

    def test_search_key_selenium(self):
        """搜索关键字: selenium """
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title,"selenium_百度搜索")

    def test_search_key_unittest(self):
        """搜索关键字: unittest """
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(("unittest"))
        self.driver.find_element_by_id("su").click()
        sleep(2)
        title=self.driver.title
        self.assertEqual(title,"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
