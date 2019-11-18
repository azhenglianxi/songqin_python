from appium import webdriver
import time, traceback

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'testxxx',
    'app': r'd:\apk\duoduoCalculators.apk',
    'appPackage': 'com.ibox.calculators',
    'appActivity': 'com.ibox.calculators.SplashActivity',
    'noReset': True,
    'newCommandTimeout': 6000,
    #'unicodeKeyboard': True
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.implicitly_wait(10)
#3
# driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/digit3"]').click()

driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.ibox.calculators:id/digit3")').click()

ele=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").instance(1)')
print(ele.text)
print(ele.location)
print(ele.size)

#+
driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/plus"]').click()
#9
driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/digit9"]').click()
#=
equal=driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/equal"]')
equal.click()
#*
driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/mul"]').click()
#5
driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/digit5"]').click()
#=
equal.click()

# relate=driver.find_element_by_xpath('com.ibox.calculators:id/cv')
# res=relate.find_elements_by_class_name('android.widget.TextView')[1]
res2=driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]')

if res2.text == '60':
    print('pass')
else:
    print('fail')

input('..........')


driver.quit()


