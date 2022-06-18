#-*-coding: utf-8-*-
#@Time  :2021/12/25 6:22
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: fixture.py
import unittest

def setUpModule():
    print("test module start >>>>>>>>>>>>>>>")

def tearDownModule():
    print("test module end >>>>>>>>>>>>>>>>>")

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test class start =============>")

    @classmethod
    def tearDownClass(cls):
        print("test class end ==================>")

    def setUp(self):
        print("test case start -->")

    def tearDown(self):
        print("test case end -->")

    def test_case1(self):
        print("test case1")

    def test_case2(self):
        print("test case2")

if __name__ == "__main__":
    unittest.main()