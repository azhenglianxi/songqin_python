#!/usr/bin/env python
#@Time     :2019-11-08 21:21:11  
#@Author   :azhenglianxi

from appium import webdriver

desired_caps ={
    "platformName": "Android",
    "platformVersion": '9',
    "deviceName": "test",
    "appPackage": "com.kuaishou.nebula",
    "appActivity": "com.yxcorp.gifshow.HomeActivity",
     'app': r'D:\install_package\com.yxcorp.gifshow.App.apk',
    "noRest":True,
    "newcommandTimeout":6000,
    "automationName":"UiAutomator2"

}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
input(1222121)
driver.quit()