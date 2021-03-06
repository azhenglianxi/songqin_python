from appium import webdriver
import time,sys

desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6',
            'deviceName': 'xxxxx',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'noReset': True,
            'newCommandTimeout' : 6000,
            'automationName':'UIAutomator2',
            }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)

#点击底部微信菜单
driver.find_element_by_android_uiautomator('text("微信")').click() #点击微信Tab


def verticalScroll(start,end):
    w = driver.get_window_size()['width']
    h = driver.get_window_size()['height']
    x = int(w /2 )  # x坐标
    y1 = int(h * end )  # 起点y坐标
    y2 = int(h * start)  # 终点y坐标
    driver.swipe(x, y1, x, y2, 2000)

#  向下滑动屏幕，进入小程序界面
verticalScroll(0.75,0.25)

# 找到小程序
driver.find_element_by_android_uiautomator('textStartsWith("星巴克")').click()

# 等待界面出现
# driver.find_element_by_id('com.tencent.mm:id/oa')
time.sleep(3)

verticalScroll(0.3, 0.8)
time.sleep(1)
verticalScroll(0.3, 0.8)
time.sleep(1)

driver.find_element_by_android_uiautomator('text("咖啡有你")').click()

time.sleep(3)

ele = driver.find_element_by_xpath("//*[@text='红茶拿铁']/../../../android.view.View[2]")

ele.click()

time.sleep(1)

driver.find_element_by_xpath("//*[@text='购买 ']").click()
input('ok')



