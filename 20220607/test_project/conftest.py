#-*-coding: utf-8-*-
#@Time  :2022/6/7 6:54
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: conftest.py

import pytest

@pytest.fixture()
def test_url():
    return "http://www.baidu.com"