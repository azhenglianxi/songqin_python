from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'D:\Users\下载\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    # 根据id找到元素，并点击，id和 html 元素的id不同
    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/tv_tab_title").click()
    time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id('io.manong.developerdaily:id/edt_phone')
    ele.send_keys('17854209376')
    driver.find_element_by_id('io.manong.developerdaily:id/btn_send_verifycode').click()
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_code")
    ele.send_keys(input("请输入验证码："))

    time.sleep(2)
    # 点击登录
    driver.find_element_by_id('io.manong.developerdaily:id/btn_login').click()
    pass

except:
    print (traceback.format_exc())


input('**** Press to quit..')
driver.quit()
