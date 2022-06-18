#-*-coding: utf-8-*-
#@Time  :2021/12/22 5:27
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: calculator.py
import importlib
class Calculator:
    """用于完成两个数的加、减、乘、除"""
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    #乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b