from appium import webdriver
import  time

desired_caps ={
    "platformName": "Android",
    "platformVersion": "8",
    "deviceName": "test",
    "appActivity": "com.alipay.mobile.quinox.LauncherActivity",
    "appPackage": "com.qdccb.bank",
   # "app": r'D:\Install_package\app-debug.apk',
    'noReset': "True"



}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(4)
driver.tap([140,800])
driver.implicitly_wait(4)
