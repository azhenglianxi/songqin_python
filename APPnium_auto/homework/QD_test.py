from appium import webdriver
import  time

desired_caps ={
    "platformName": "Android",
    "platformVersion": 9,
    "deviceName": "test",
    "app": "D:\\install_package\\directbank_online_face_next_login0715-release.apk",
    "appActivity": "com.yuchengnet.android.directbank.SplashActivity",
    "appPackage": "com.yuchengnet.android.directbank",
    "noRest": True,
    "newcommandTimeout": 600,
    "automationName": "UiAutomator2"


}
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)