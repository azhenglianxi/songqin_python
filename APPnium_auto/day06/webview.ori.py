# coding=utf8
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {
    'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '6',
    'deviceName': 'test',
    'appPackage': 'com.example.jcy.wvtest',
    'appActivity': '.MainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'chromedriverExecutableDir':r'D:\tools\webdrivers\chromedriver_win32_v2.23',
    'noReset': True,
    'newCommandTimeout': 6000,
    # 'chromedriverExecutable':r'D:\tools\webdrivers\chromedriver_win32_v2.23\chromedriver.exe'
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)
try:
    print(driver.contexts)
    print(driver.current_context)  # 当前的cuntext
    driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')
    print(driver.current_context)#当前的cuntext
    driver.find_element_by_id('index-kw').send_keys('松勤\n')

    driver.switch_to.context('NATIVE_APP')
    driver.find_element_by_accessibility_id('面板').click()
    driver.find_element_by_accessibility_id('通知').click()

except:
    print (traceback.format_exc())


input('**** Press to quit..')
driver.quit()