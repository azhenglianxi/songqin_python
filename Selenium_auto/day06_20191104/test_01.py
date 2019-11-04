#!/usr/bin/env python
#@Time     :2019-11-01 21:09:01   #@Author   :azhenglianxi   
#@Software :PyCharm

from Selenium_auto.funtion_Interface import *
driver =ChromeDriverBrowser()



#要切换窗口
handle=driver.window_handles
for handle in handle:
    driver.switch_to.window(handle)
    if '内容' in driver.title:
        break
#driver.switch_to.window(main_hadle）


#弹出对话框解决方案  # alreat
#触发alert
driver.find_element_by_id('b3').click()

driver.switch_to.alert.send_keys('hello promot')

al =driver.switch_to.alert.accept()

#al.dismiss()  #点击取消
#al.accept() #点击确定



#点击取消 congfilm 的输入弹框
driver.find_element_by_id('b3').click()
#输入框操作
al.send_keys('sdsd')
#input 输入操作
print(al)
#清楚操作
al.dismiss()



#模拟滚动界面
for i  in range(5):
    driver.execute_script('window.scrollBy(0,500)')
    time.sleep(1)
    if driver.find_elements_by_css_selector('xxxx'):
        print()