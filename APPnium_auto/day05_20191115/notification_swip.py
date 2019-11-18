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

    time.sleep(5)

    screenSize = driver.get_window_size()
    screenW = screenSize['width']
    screenH = screenSize['height']

    x = screenW / 2
    y1 = int(screenH * 0.1)
    y2 = int(screenH * 0.8)
    driver.swipe(start_x=x, start_y=5, end_x=x, end_y=y2, duration=300)

    time.sleep(1)
    eles = driver.find_elements_by_xpath('//android.widget.LinearLayout[@resource-id="android:id/line1"]/android.widget.TextView[@resource-id="android:id/title"]')

    for ele in eles:
        print(ele.text)

    time.sleep(2)


    driver.press_keycode(4)
    #
    # time.sleep(2)
    # driver.press_keycode(27)

    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()