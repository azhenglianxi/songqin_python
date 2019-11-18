#!/usr/bin/env python
#@Time     :2019-11-13 20:14:45  
#@Author   :azhenglianxi

from appium import webdriver

desired_caps ={
  "platformName": "Android",
  "platformVersion": "6",
  "deviceName": "test",
  "appActivity": "io.toutiao.android.ui.activity.LaunchActivity",
  "app": "r'D:\\Users\\下载\\toutiao.apk'",
  "appPackage": "io.manong.developerdaily",
  "noRest": True,
  "newcommandTimeout": 6000,
   "automationName":"UiAutomator2"


}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)