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

screen_size=driver.get_window_size()
x1=screen_size['width']/2#中点
y1=screen_size['height']/2#中点

res=[]
#连续滚动屏幕，直到发现口碑最佳
driver.implicitly_wait(0.5)
while 1:
    driver.swipe(x1,y1,x1,y1-500,500)
    #一遍滑动，一边找口碑最佳
    kb=driver.find_elements_by_accessibility_id('best reputation')
    if kb:
        #开始保存app名称
        kb_apps=driver.find_elements_by_xpath('//*[@content-desc="best reputation"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]')
        #保存新增的app名称
        tmp=[kb.text for kb in kb_apps]
        # for e in tmp:
        #     if e not in res:
        #         res.append(e)
        res.extend(tmp)


    #还要发现用户最爱来停止滑动
    zuiai = driver.find_elements_by_accessibility_id('user favorite')
    if zuiai:
        break

driver.implicitly_wait(10)


# print(set(res))
print(res)

driver.quit()

