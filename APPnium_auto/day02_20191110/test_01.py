#!/usr/bin/env python
#@Time     :2019-11-08 21:21:11  
#@Author   :azhenglianxi

from appium import webdriver

desired_caps ={
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "test",
  "appActivity": "io.toutiao.android.ui.activity.LaunchActivity",
  #'app': r'D:\Users\下载\toutiao.apk',
  "appPackage": "io.manong.developerdaily",
  "noRest": True,
  "newcommandTimeout": 6000,
  "automationName":"UiAutomator2"


}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
# eles =driver.find_elements_by_id('io.manong.developerdaily:id/ll_tap')
#利用上层元素查找
p_else =driver.find_element_by_id('io.manong.developerdaily:id/tab_bar_container')
target_eles =p_else.find_elements_by_id('tv_tab_title')
for ele in target_eles:
    if p_else.text =='我的':
        print('找到元素')
        ele.click()
driver.find_element_by_accessibility_id('通知')

input(1222121)
driver.quit()