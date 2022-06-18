#-*-coding: utf-8-*-
#@Time  :2021/10/8 6:32
#@Author: sixiaoyou
#@Email: 834628301@qq.com
#@File: 多窗口切换.py

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获得百度搜索窗口句柄
search_windows=driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

#获得当前所有打开的窗口句柄
all_handles=driver.window_handles

#进入注册窗口
for handle in all_handles:
    if __name__ == '__main__':
        if handle != search_windows:
            driver.switch_to_window(handle)
            print(driver.title)
            driver.find_element_by_name("username").send_keys('username')
            driver.find_element_by_name('phone').send_keys('138xxxxxxxx')
            time.sleep(2)
            #....
            #关闭当前窗口
            driver.close()
#回到搜索窗口
driver.switch_to.window(search_windows)
print(driver.title)

driver.quit()
