#-*-coding: utf-8-*-
#@Time  :2021/12/23 5:43
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: leap_year.py
class LeapYear:
    def __init__(self,year):
        self.year = int(year)

    def answer(self):
        year = self.year
        if year%100==0:
            if year&400==0:
                #整百年能被400整除的是闰年
                return "{0}是闰年".format(year)
            else:
                return "{0}不是闰年".format(year)
        else:
            if year%4==0:
                #非整百年能被4整除的是闰年
                return "{0}是闰年".format(year)
            else:
                return "{0}不是闰年".format(year)