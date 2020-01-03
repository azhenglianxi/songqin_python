#!/usr/bin/env python
#@Time     :2019-10-28 15:08:11   #@Author   :azhenglianxi   
#@Software :PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_weBdriver='D:\\Users\\azhenglianxi\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\chromedriver.exe'
firox_webDriver ='D:\\Users\\azhenglianxi\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\geckodriver.exe'
Ie_weBdriver='D:\\Users\\azhenglianxi\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\IEDriverServer.exe'
#谷歌——无界面    D:\Users\azhenglianxi\AppData\Local\Programs\Python\Python37\Scripts


def ChromeDrverNObroews():
    chrome_options =Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('disable-gpu')
    driverChrome =webdriver.Chrome(chrome_weBdriver,chrome_options=chrome_options)
    return driverChrome

#谷歌 ——有界面
def ChromeDriverBrowser():
    driverChrome = webdriver.Chrome(chrome_weBdriver)
    return driverChrome



#------------------ 未尝试--------
#火狐———有界面
def FiroxDriverBrowser():
    driverFirox =webdriver.Firefox(firox_webDriver)
    return  driverFirox

#火狐—无界面
def FiroxDrverNObroews():
    firox_options = Options()
    firox_options.add_argument('--headless')
    firox_options.add_argument('disable-gpu')
    driverfirox = webdriver.Firefox(firox_webDriver,firefox_options=firox_options )
    return firox_options



#IE --无界面
# def IeDriverNObroews():
#     IE_options = Options()
#     IE_options.add_argument('--headless')
#     IE_options.add_argument('disable-gpu')
#     driverIe = webdriver.Ie(Ie_weBdriver, ie_options=IE_options)
#     return IE_options

#IE --有界面

def IeDriverBrowser():
    driverIe =webdriver.Ie()
    return  driverIe


