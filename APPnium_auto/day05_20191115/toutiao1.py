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

    code = 'new UiSelector().resourceId("io.manong.developerdaily:id/tab_bar").childSelector(new UiSelector().className("android.widget.TextView").instance(3))'
    ele = driver.find_element_by_android_uiautomator(code)

    ele.click()

    time.sleep(2)

    # 耗时特别长
    try:
        driver.start_activity('com.example.jcy.wvtest',
                          '.MainActivity',
                          )
    except:
        pass

    # ele = driver.find_element_by_id('com.huawei.appmarket:id/banner')

    # 返回开发者头条
    try:
        driver.start_activity('io.manong.developerdaily',                              'io.toutiao.android.ui.activity.LaunchActivity',
                              )
    except:
        pass

    time.sleep(2)
    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()