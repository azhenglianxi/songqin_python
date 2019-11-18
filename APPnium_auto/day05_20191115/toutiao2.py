# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {
    'automationName': 'uiautomator2',
    'platformName': 'Android',
    'platformVersion': '6',
    'deviceName': 'test',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'io.manong.developerdaily',
    'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard':True,
    'noReset': True,
    'newCommandTimeout': 6000
}
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    # -----------------
    code = 'new UiSelector().text("发现").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(code).click()
    time.sleep(2)

    driver.implicitly_wait(1)
    while True:
        driver.swipe(400,800,400,300,2000)

        code = 'new UiSelector().text("已经全部加载完毕").className("android.widget.TextView")'
        eles = driver.find_elements_by_android_uiautomator(code)
        if eles:
            break

    driver.implicitly_wait(10)
    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()


