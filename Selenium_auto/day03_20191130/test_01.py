#!/usr/bin/env python
#@Time     :2019-10-30 17:22:08   #@Author   :azhenglianxi   
#@Software :PyCharm
from Selenium_auto.funtion_Interface import *
#Selenium 等待元素出现  + frame 界面切换 +css

#css 定位选择器
# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///D:/Users/azhenglianxi/songqin_python/Selenium_auto/if.html')

driver.switch_to.frame('baidu')
driver.find_element_by_id('kw').send_keys('松勤\n')

#切回主HTML
driver.switch_to.default_content()
driver.find_element_by_tag_name('input')







# driver.switch_to.frame('baidu')
# kw = driver.find_element_by_id("kw")
# kw.send_keys(u'松勤\n')
#
# driver.switch_to.default_content()
# input1 = driver.find_element_by_tag_name("input")
# input1.send_keys('hello world')

input('press any key to quit...')
driver.quit()
