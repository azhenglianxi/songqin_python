#!/usr/bin/env python
#@Time     :2019-10-31 10:39:37   #@Author   :azhenglianxi   
#@Software :PyCharm

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///D:/Users/azhenglianxi/songqin_python/Selenium_auto/nested.html')

#切到内1层
driver.switch_to.frame('layer2')
#切到内2层
driver.switch_to.frame('layer3')

driver.find_element_by_tag_name('input').send_keys('内2层输入')


#切到最外层
#driver.switch_to.default_content()

#切到上一层
driver.switch_to.parent_frame()

driver.find_element_by_tag_name('input').send_keys('内1层输入')