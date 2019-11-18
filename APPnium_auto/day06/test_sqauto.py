from appium import webdriver

desired_caps = {
    'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '6',
    'deviceName': 'glaxy5',
    'appPackage': 'com.sqauto',
    'appActivity': 'com.sqauto.MainActivity',
    'noReset': True,
    'newCommandTimeout': 6000,
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

size=driver.get_window_size()

x=size['width']*0.5
y1=size['height']*0.6

res=[]
driver.implicitly_wait(0)
while 1:
    driver.swipe(x,y1,x,y1-size['height']*0.2,500)
    kb=driver.find_elements_by_accessibility_id('best reputation')
    if kb:
        xpath='//*[@content-desc="best reputation"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]'
        kb_app=driver.find_elements_by_xpath(xpath)
        res.extend([ele.text for ele in kb_app])
    #发现用户最爱就停止滑动
    za=driver.find_elements_by_accessibility_id('user favorite')
    if za:
        break
driver.implicitly_wait(10)
#假如后面还有其他的找元素操作

print('口碑最佳的应用有：')
[print(one) for one in set(res)]


driver.quit()