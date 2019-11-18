# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    # -----------------
  #关闭通知栏
    #1.通过滑动屏幕实现

    # raw_input('press to check notification...')
    driver.open_notifications()
    time.sleep(1)
    eles = driver.find_elements_by_xpath('//com.android.systemui.statusbar.phone.TimeAxisWidgetEx//android.widget.TextView')

    texts = []
    for ele in eles:
        t =  ele.text
        texts.append(t)


    if u'''江春阳|hello''' in '|'.join(texts):
        print('pass')
    else:
        print( 'failed')

    screenSize = driver.get_window_size()
    screenW = screenSize['width']
    screenH = screenSize['height']

    x = screenW / 2
    y1 = int(screenH * 0.8)
    y2 = int(screenH * 0.4)
    driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=300)

    # -----------------

except:
    print(traceback.format_exc())
    # 2.通过按下返回键 实现
    time.sleep(5)
    driver.keyevent(4) #表示按下返回键

input('sdasdas')
driver.quit()
#利用按键条件屏幕亮度  变亮 变暗
for i in  range(5):
    driver.keyevent(220)
    time.sleep(0.5)
for i in  range(5):
    driver.keyevent(221)
    time.sleep(0.5)
