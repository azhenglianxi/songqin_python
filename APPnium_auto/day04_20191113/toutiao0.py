# coding=utf8

from appium import webdriver
import time,traceback


desired_caps = {
    #'automationName': 'uiautomator2',
    'platformName': 'Android',
    'platformVersion': '6.50',
    'deviceName': 'test',
    #'app': r'D:\Users\下载',
    'appPackage': 'io.manong.developerdaily',
    'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset': True,
    'newCommandTimeout': 6000
}

#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:

    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("io.manong.developerdaily:id/iv_tab_icon")')

except:
    print(traceback.format_exc())
input('**** Press to quit..')
driver.quit()