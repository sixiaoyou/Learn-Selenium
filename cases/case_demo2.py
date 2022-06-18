#-*-coding: utf-8-*-
#@Time  :2022/1/2 10:32
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: case_demo2.py
'''
测试代码的编写
'''
from web_keys.keys1 import Key

key = Key('Chrome')
key.open('http://www.baidu.com')
key.input('id','kw','虚竹2.0')
key.click('id','su')