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
            # 'unicodeKeyboard': True,
            # 'resetKeyboard':True,
            }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)

#进入星巴克小程序
size=driver.get_window_size()
width=size['width']
height=size['height']
#确保载入微信界面
driver.find_element_by_id('com.tencent.mm:id/ddm')


driver.swipe(width*0.5,height*0.2,width*0.5,height*0.8)

driver.find_element_by_xpath('//android.widget.TextView[@text="星巴克用星说"]').click()

time.sleep(20)#等待小程序加载

#找到咖啡有你-点击进入
while 1:
    driver.swipe(width*0.5,height*0.8,width*0.5,height*0.2)
    coffe=driver.find_elements_by_xpath('//android.view.View[@text="咖啡有你"]')
    if coffe:
        # coffe[0].click()
        break
time.sleep(3)
driver.find_element_by_xpath('//android.widget.Button[contains(@text,"咖啡")]').click()

driver.tap([(300,1300)],3000)#长按效果


#等待页面加载
time.sleep(10)

#找到美食咖啡
while 1:
    driver.swipe(width*0.5,height*0.8,width*0.5,height*0.2)
    coffe=driver.find_elements_by_xpath('//android.view.View[@text="使用须知"]')
    if coffe:
        driver.find_element_by_xpath('//android.view.View[@text="美式咖啡"]/following-sibling::android.view.View[2]').click()
        break

time.sleep(1)

driver.find_element_by_xpath('//android.widget.Button[@text="购买 "]').click()

time.sleep(5)

#确定购买
driver.find_element_by_id('com.tencent.mm:id/fpv').click()

driver.quit()

