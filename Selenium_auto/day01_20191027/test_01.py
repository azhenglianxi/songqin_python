#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time     :2019-10-26 22:38:41
#@Author   :azhenglianxi
#@Site     :
#@File     :test_01.py
#@Software :PyCharm

import time
from selenium import webdriver
driver =webdriver.Chrome(r'D:\Users\azhenglianxi\AppData\Local\Programs\Python\Python37\Scripts\chromedriver.exe')
driver.get('https://www.baidu.com/')
ele=driver.find_element_by_id('kw')
ele.send_keys('松勤\n')
#测试第一条记录 包含——松勤 - 松勤软件测试
res=driver.find_element_by_id('1')
if '松勤 - 松勤软件测试' in res.text:
    print('pass')
else:
    print('fail')
#res.find_element_by_tag_name() # 根据标签查找元素
#assert '松勤网-松勤软件测试' in res.text
time.sleep(3)
driver.close() #关闭窗口
driver.quit()  #关闭浏览器



