#-*-coding: utf-8-*-
#@Time  :2022/6/7 5:30
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: test_sample.py
import pytest


def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5


if __name__ == '__main__':
    pytest.main()