#!/usr/bin/env python
#@Time     :2019-11-08 21:21:11  
#@Author   :azhenglianxi

from appium import webdriver

desired_caps ={
    "platformName": "Android",
    "platformVersion": "9.0",
    "deviceName": "test",
    "appActivity":"io.toutiao.android.ui.activity.LaunchActivity",
    "appPackage":"io.manong.developerdaily",
    'app': r'D:\Users\下载\toutiao.apk',
    "noRest":True,
    "newcommandTimeout":6000,
    "automationName":"UiAutomator2"


}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)



input(1222121)
driver.quit()