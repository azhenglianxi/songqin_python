# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {
    'automationName': 'uiautomator2',
    'platformName': 'Android',
    'platformVersion': '6',
    'deviceName': 'test',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'com.sqauto',
    'appActivity': 'com.sqauto.MainActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard':True,
    'noReset': True,
    'newCommandTimeout': 6000
}
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(10)

try:
    #滚动页面找到口碑最佳
    w_size=driver.get_window_size()
    x1=w_size['width']/2
    y1=w_size['height']/2
    total_apps=[]
    while 1:
        driver.swipe(x1,y1,x1,y1-500,500)
        #找到口碑最佳后开始收集应用名称
        kb=driver.find_elements_by_accessibility_id('best reputation')
        if kb:
            #搜集app名称
            apps=driver.find_elements_by_xpath('//*[@text="口碑最佳"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]')
            print([app.text for app in apps])

            total_apps.extend(apps)#汇总app

    #不断获取口碑最佳的应用，直到发现用户最爱
        zuai=driver.find_elements_by_accessibility_id('user favorite')
        if zuai:
            apps2=driver.find_elements_by_xpath('//*[@text="用户最爱"]/preceding-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]')
            total_apps.extend(apps2)  # 汇总app
            break

    #打印目标app名称
    print(set(app.text for app in total_apps))


except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()


