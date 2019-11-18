# coding=utf8
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {
    # 'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'test',
    'browserName':'Chrome',
    'chromedriverExecutableDir':r'D:\Users\azhenglianxi\AppData\Local\Programs\Python\Python37\Scripts\chromedriver.exe',
    'newCommandTimeout': 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(20)
#启动手机里的浏览器
try:
    print(driver.current_context)#查看当前处于原生还是webview
    print(driver.contexts)#查看所有的context
    driver.get('http://baidu.com')

    driver.switch_to.context('NATIVE_APP')
    print(driver.current_context)
    btns=driver.find_elements_by_id('negative_button')  # 点禁止定位
    if btns:
        btns[0].click()
    time.sleep(2)

    #我们再根据对应的情况来处理
    #如果是原生，我们就要切换到webview里面操作网页
    if driver.current_context =='NATIVE_APP':
        driver.switch_to.context('CHROMIUM')

    print(driver.current_context)
    driver.find_element_by_id('index-kw').send_keys('松勤\n')

    # driver.switch_to.context('NATIVE_APP')

    time.sleep(5)






    # driver.implicitly_wait(10.0)
    # driver.get('http://www.baidu.com')
    # print(driver.contexts)
    # print(driver.current_context)
    #
    # driver.find_element_by_id('index-kw').send_keys('松勤\n')
    #
    # # driver.find_element_by_id('index-bn').click()
    # time.sleep(3)
    # # 如果出现定位弹出框，需要切换到原生部分点击按钮
    # driver.switch_to.context('NATIVE_APP')
    # driver.find_element_by_id('com.android.chrome:id/negative_button').click()

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()