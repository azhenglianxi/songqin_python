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

    driver.open_notifications()

    time.sleep(3)
    #返回
    driver.press_keycode(4)
    time.sleep(2)
    #调音量
    driver.press_keycode(24)
    time.sleep(2)
    driver.press_keycode(25)
    key_power=26
    #长按
    driver.long_press_keycode(key_power)





    #KEYCODE_BACK=4
    # driver.press_keycode(4)
    #
    # #控制音量+KEYCODE_VOLUME_UP
    # for i in range(5):
    #     driver.press_keycode(24)
    #
    # #KEYCODE_BRIGHTNESS_DOWN=220
    # for i in range(5):
    #     driver.press_keycode(220)



    # time.sleep(1)
    # xpath='//*[@resource-id="android:id/notification_main_column"]//*[@resource-id="android:id/title"]|//*[@resource-id="com.sec.android.app.samsungapps:id/noti_title"]'
    # eles = driver.find_elements_by_xpath(xpath)
    #
    # for ele in eles:
    #     print(ele.text)
    #
    # time.sleep(5)
    #
    # #KEYCODE_BACK
    # driver.press_keycode(4)
    #
    # #KEYCODE_VOLUME_DOWN
    # for i in range(5):
    #     driver.press_keycode(25)
    #     time.sleep(1)


    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()