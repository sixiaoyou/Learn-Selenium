#-*-coding: utf-8-*-
#@Time  :2021/12/20 5:55
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 处理HTML5视频播放.py

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://videojs.com/")

video = driver.find_element_by_id("preview-player_html5_api")

# 返回播放文件地址
url=driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print("start")
driver.execute_script("arguments[0].play()",video)

#播放15秒
sleep(15)

#暂停视频
print("stop")
driver.execute_script("arguments[0].pause()",video)

driver,quit()
