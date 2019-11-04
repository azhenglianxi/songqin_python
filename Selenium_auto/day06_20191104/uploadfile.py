
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

#先到目标页面
driver.get('https://tinypng.com/')

driver.find_element_by_css_selector('.icon').click()
time.sleep(2)

#开始上传文件

import win32com.client  #安装win 控件
import win32api
import  win32con

shell=win32com.client.Dispatch("WScript.Shell")  #enter 的数字按键
shell.SendKeys(r'D:\banner.png'+'\n')

win32api.keybd_event(win32con.VK_ADD,0)








# driver.find_element_by_css_selector('.icon').click()
# time.sleep(2)
# # 直接发送键盘消息给 当前应用程序，
# # 前提是浏览器必须是当前应用
# #   pip install pypiwin32
#
# import win32com.client
#
# shell=win32com.client.Dispatch("WScript.Shell")
#
# shell.Sendkeys(r'd:\baidu.png'+'\n')





input('...')

driver.quit()