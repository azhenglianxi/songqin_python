#!/usr/bin/env python
#@Time     :2020-01-17 10:37:49  
#@Author   :azhenglianxi   

from appium import webdriver
from time import sleep

class Action():
    def __init__(self):
        self.desired_caps={
            "platformName": "Android",
            "platformVersion": '9',
            "deviceName": "红米8",
            "appPackage": "com.kuaishou.nebula",
            "appActivity": "com.yxcorp.gifshow.HomeActivity"

        }
        self.server ="http://localhost:5555/wd/hub"
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.start_x =500
        self.start_y =1500
        self.distance =1300
    def comment(self):
        sleep(12)
        self.driver.tap([(500, 1200)], 500)
    def scroll(self):
        while True:
            self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance,300)
            # 设置延时等待
            sleep(18)
    def main(self):
        self.comment()
        self.scroll()
if __name__ == '__main__':
    action = Action()
    action.main()

