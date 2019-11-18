from appium import webdriver
import time,sys

desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6',
            'deviceName': 'xxxxx',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'noReset': True,
            'newCommandTimeout' : 6000,
            'automationName':'UIAutomator2',
            'unicodeKeyboard': True,
            'resetKeyboard':True,
            }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)

driver.find_element_by_xpath('//android.widget.TextView[@text="微信"]')

#向下滑动屏幕，进入小程序候选界面
size=driver.get_window_size()

x1=size['width']*0.5
y1=size['height']*0.3
y2=size['height']*0.8

driver.swipe(x1,y1,x1,y2,2000)
time.sleep(2)

#点击星巴克小程序
driver.find_element_by_xpath('//android.widget.TextView[@text="星巴克用星说"]').click()


#操作星巴克小程序
time.sleep(15)

#下拉寻找咖啡有你
y2=size['height']*0.5
driver.implicitly_wait(0.5)
while 1:
    driver.swipe(x1,y2,x1,y2-600,1000)
    time.sleep(1)
    coffe=driver.find_elements_by_xpath('//android.view.View[@text="咖啡有你"]')
    if coffe:
        driver.find_element_by_xpath('//android.widget.Button[contains(@text,"咖啡")]').click()
        break

time.sleep(10)

# 选择美式咖啡
while 1:
    driver.swipe(x1,y2,x1,y2-600,1000)
    time.sleep(1)
    coffe=driver.find_elements_by_xpath('//android.view.View[@text="美式咖啡"]')
    if coffe:
        driver.find_element_by_xpath('//android.view.View[@text="美式咖啡"]/following-sibling::android.view.View[2]').click()
        break



time.sleep(2)
driver.implicitly_wait(15)

#点击购买

driver.find_element_by_xpath('//android.widget.Button[@text="购买 "]').click()
time.sleep(3)

#确认购买

# driver.find_element_by_xpath('//android.widget.Button[@text="立即支付"]').click()

driver.find_element_by_id('com.tencent.mm:id/ffu').click()




time.sleep(30)
driver.quit()





