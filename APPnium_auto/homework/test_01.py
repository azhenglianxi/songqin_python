#!/usr/bin/env python
#@Time     :2019-11-10 11:44:57  
#@Author   :azhenglianxi   



from appium import webdriver
import  time

desired_caps ={
  "platformName": "Android",
  "platformVersion": "8",
  "deviceName": "test",
   "app": "D:\\Users\\下载\\com.ibox.calculators_3.1.0_1310.apk",
  "appActivity": "com.ibox.calculators.SplashActivity",
  "appPackage": "com.ibox.calculators",
  "noRest": True,
  "newcommandTimeout": 6000
   # "automationName":"UiAutomator2"


}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
time.sleep(6)

three=driver.find_element_by_id('com.ibox.calculators:id/digit3').click()
puls =driver.find_element_by_id('com.ibox.calculators:id/plus').click()
nine =driver.find_element_by_id('com.ibox.calculators:id/digit9').click()
dengyu =driver.find_element_by_id('com.ibox.calculators:id/equal').click()
time.sleep(1)
cheng =driver.find_element_by_id('com.ibox.calculators:id/mul').click()
five =driver.find_element_by_id('com.ibox.calculators:id/digit5').click()
driver.find_element_by_id('com.ibox.calculators:id/equal').click()
wer=driver.find_element_by_id('com.ibox.calculators:id/cv')
res=wer.find_elements_by_class_name('android.widget.TextView')
print(res)
retStr = res[1].text



print(res)
if retStr =='60':
    print('测试通过1')

