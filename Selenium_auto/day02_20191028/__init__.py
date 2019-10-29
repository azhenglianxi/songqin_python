#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time     :2019-10-27 12:03:25
#@Author   :azhenglianxi
#@Site     :
#@File     :__init__.py.py
#@Software :PyCharm

from Selenium_auto.funtion_Interface import *
import  time

driver =ChromeDriverBrowser()
driver .get('https://www.baidu.com')
e_size=driver.get_window_position()
print(e_size)
#s_X_Y =driver.set_window_position()#需要传入参数
#print(s_X_Y)
lix=driver.find_element_by_link_text("新闻")
sss=lix.get_attribute('href')
ss=lix.get_attribute('style')
print(sss+ss)
rn =driver.find_element_by_name('rn').is_displayed()
print(rn)
input(' .....')
driver.close()