#-*-coding: utf-8-*-
#@Time  :2021/12/23 6:03
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: run_tests.py
import unittest

#定义测试用例的目录为当前目录中的test_case/目录
test_dir ='../20211220'
suits=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(suits)