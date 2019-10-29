#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time     :2019-10-27 12:03:44
#@Author   :azhenglianxi
#@Site     :
#@File     :test_01.py
#@Software :PyCharm


#get_attribute()#获取某个属性值
##get_attribute('outerHTML')#获取整个元素HTML文本
#get_attribute('innerHTMl')#获取内部元素HTML


#.get_attribute('innerText')

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('file:///D:/Users/azhenglianxi/songqin_python/Selenium_auto/s1.html')
lix= driver.find_element_by_link_text('新闻')
print(lix)


