#!/usr/bin/env python
#@Time     :2019-10-28 15:08:11   #@Author   :azhenglianxi   
#@Software :PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_weBdriver='D:\\Users\\azhenglianxi\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\chromedriver.exe'

#无界面

def ChromeDrverNObroews():
    chrome_options =Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('disable-gpu')
    driverChrome =webdriver.Chrome(chrome_weBdriver,chrome_options=chrome_options)
    return driverChrome

#有界面
def ChromeDriverBrowser():
    driverChrome = webdriver.Chrome(chrome_weBdriver)
    return driverChrome


