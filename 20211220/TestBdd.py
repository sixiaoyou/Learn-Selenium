#-*-coding: utf-8-*-
#@Time  :2021/12/24 5:26
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: TestBdd.py
import unittest
import importlib

class TestBdd(unittest.TestCase):

    def setUp(self):
        print("test TestBdd:")

    def test_ccc(self):
        print("test ccc")

    def test_aaa(self):
        print("test aaa")

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test TestAdd:")

    def test_bbb(self):
        print("test bbb")

# if __name__ == "__main__":
#     unittest.main()

if __name__=="__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestBdd("test_aaa"))
    suite.addTest(TestBdd("test_ccc"))
    suite.addTest(TestAdd("test_bbb"))

    runner = unittest.TextTestRunner()
    runner.run(suite)

