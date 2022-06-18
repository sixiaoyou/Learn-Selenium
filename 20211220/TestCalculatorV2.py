#-*-coding: utf-8-*-
#@Time  :2021/12/22 6:09
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: TestCalculatorV2.py
from calculator import Calculator
import unittest
import importlib

class TestCalculatorV2(unittest.TestCase):
    #测试用例前置动作
    def setUp(self):
        print("test start:")

    #测试用例后置动作
    def tearDown(self):
        print("test end")

    def test_add(self):
        c = Calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator(7, 2)
        result = c.sub()
        self.assertEqual(result, 5)

    def test_mul(self):
        c = Calculator(3, 3)
        result = c.mul()
        self.assertEqual(result, 10)

    def test_div(self):
        c = Calculator(6, 2)
        result = c.div()
        self.assertEqual(result, 3)

if __name__ == '__main__':
        #创建测试套件
        suit = unittest.TestSuite()
        suit.addTest(TestCalculatorV2("test_add"))
        suit.addTest(TestCalculatorV2("test_sub"))
        suit.addTest(TestCalculatorV2("test_mul"))
        suit.addTest(TestCalculatorV2("test_div"))

        #创建测试运行器
        runner = unittest.TextTestRunner()
        runner.run(suit)

