from appium import webdriver
import  time

desired_caps ={
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "test",
    "app": "D:\\Users\\下载\\app-sitq2-1118.apk",
    "appPackage": "com.qdccb.bank",
    "appActivity": "com.alipay.mobile.quinox.LauncherActivity",
    "noReset": True,
    "newCommandTimeout": 5000,
    "unicodeKeyboard": True


}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)