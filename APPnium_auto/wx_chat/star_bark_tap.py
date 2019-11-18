from appium import webdriver
import time,sys
from .tap_cfg import *



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

#通过坐标操作

driver.swipe(x1,y2,x1,y1,2000)
time.sleep(2)
#点击咖啡有你
driver.tap([(size['width']*0.75,y2)])
time.sleep(10)


#选择美式咖啡
driver.swipe(x1,y2,x1,y1,2000)
driver.swipe(x1,y2,x1,y1,2000)
time.sleep(2)

if '1080'== cod:
    btn=click_btn['1080p']
else:
    btn=(click_btn['720'])

driver.tap([btn])

time.sleep(30)
driver.quit()





