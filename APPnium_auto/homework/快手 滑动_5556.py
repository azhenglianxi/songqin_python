#!/usr/bin/env python
#@Time     :2020-01-17 10:37:49  
#@Author   :azhenglianxi   

from appium import webdriver
from time import sleep

class Action():
    def __init__(self):
        self.desired_caps={
            "platformName": "Android",
            "platformVersion": '8',
            "deviceName": "红米8",
            "appActivity": "com.yxcorp.gifshow.HomeActivity",
            #'unicodeKeyboard': "True",  # 使用unicode输入法
           # 'resetKeyboard': "True",  # 重置输入法到初始状态XXXXXXXXXXXXXXXXRRRRRRRR
            'noReset': "True"  # 启动app时不要清除app里的原有的数据

        }
        self.server ="http://localhost:5556/wd/hub"   # adb -s 6de469bd tcpip 5556
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.start_x =500
        self.start_y =1500
        self.distance =1300
    def comment(self):
       # input("初始化手动设置..")
        sleep(4)
        self.driver.tap([(500, 1200)], 500)
    def scroll(self):
        while True:
            self.driver.swipe(self.start_x, self.start_y, self.start_x,self.start_y-self.distance,300)
            # 设置延时等待
            sleep(8)
    def main(self):
        self.comment()
        self.scroll()
if __name__ == '__main__':
    action = Action()
    action.main()

