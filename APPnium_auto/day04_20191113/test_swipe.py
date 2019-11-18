# coding=utf8
from appium import webdriver
import time
import traceback


desired_caps = {}
desired_caps['automationName'] ='UiAutomator2'
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '6'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
#desired_caps['app'] = r'd:\apk\HiSpace.apk'  #app 文件 名，指定了要安装的app 在电脑上的路径
desired_caps['appPackage'] = 'com.huawei.appmarket'  #app package名,指定了要运行的app
desired_caps['appActivity'] = 'com.huawei.appmarket.MainActivity' #app默认Activity
# desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
# desired_caps['automationName'] = 'uiautomator2'
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

try:

    # ele = driver.find_element_by_id('com.huawei.appmarket:id/commodityLL')

    banner=driver.find_element_by_id('com.huawei.appmarket:id/backPicture')

    ele_w=banner.size['width']
    move_distance=ele_w*0.6

    w=driver.get_window_size()['width']
    h=driver.get_window_size()['height']
    x1=w*0.25#宽度的1/4
    y1=h*0.3#高度的1/3
    x2=x1+move_distance
    y2=y1

    for i in range(20):
        driver.swipe(x1,y1,x2,y2,500)
        time.sleep(1)




except:
    print(traceback.format_exc())
    print('do something...')

input('**** Press to quit..')
driver.quit()


#打开通知