#!/usr/bin/env python
#@Time     :2019-10-28 20:42:06   #@Author   :azhenglianxi   
#@Software :PyCharm
from Selenium_auto.funtion_Interface import *

driver=ChromeDriverBrowser()
driver.get('https://www.baidu.com/')
ele=driver.find_element_by_id('kw')
ele.send_keys('松勤\n')

#webserver 前进后退和刷新
driver.back() # 后退

driver.forward() # 前进

driver.refresh() #刷新

driver.get_screenshot_as_file('baidu.png')#截图功能 存到当前路径

#通过元素来截图，截取得元素范围的图片  获取单个图片
ele =driver.find_element_by_id('su')
ele.screenshot(r'd:\baidu.png')

#最大化
driver.maximize_window()


#最小化
driver.minimize_window()

#设置指定的大小 固定的尺寸
driver.set_window_size(800,600)

#获取窗口的大小
size= driver.get_window_size()
print(f'高度是{size["height"]}')
print(f'高度是{size["width"]}')


#
btn = driver.find_element_by_id('su')
btn.location   #元素的坐标
e_size =btn.size
print(f'高度是{e_size["height"]}')
print(f'高度是{e_size["width"]}')

#获取窗口的位置 坐标 原点死屏幕左上角
loc =driver.get_window_position()
print(f"x:{loc['x']}y:{loc['y']}")

driver.x





#-------------webelement -------


获取