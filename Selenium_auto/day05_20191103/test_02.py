#!/usr/bin/env python
#@Time     :2019-11-01 21:43:17   0#@Author   :azhenglianxi
#@Software :PyCharm

from Selenium_auto.funtion_Interface import *
import  time
#先登录到 51.job
driver =ChromeDriverBrowser()
driver.implicitly_wait(10)

# 打开网址
driver.get('http://www.51job.com')
