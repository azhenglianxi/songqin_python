#!/usr/bin/env python
#@Time     :2019-11-01 21:43:17   #@Author   :azhenglianxi   
#@Software :PyCharm


#单元框
#怎么判断元素 是不是被选中
from selenium.webdriver.support.select import Select

##  male.clock() #来选中元素
#   if not bike.is_slelcted():
   #         bike.click()

#复选框 怎么选择
    #select 标签的
from Selenium_auto.funtion_Interface import *
driver =ChromeDriverBrowser()
se =driver.find_element_by_id('')
select=Select(se)
select.select_by_visible_text('宝马  740')
select.deselect_by_index(0) #通过下标选择 从0开始

#全选操作
select.deselect_all()   #全部取消选择
select.is_multiple


#单选下拉框
select.select_by_visible_text("女")