#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time     :2019-10-27 12:03:31
#@Author   :azhenglianxi
#@Site     :
#@File     :__init__.py.py
#@Software :PyCharm

import re
#import ele
import requests
import bs4
#爬虫的吸星大法 上面几个语句的搭配可以下载万物啦


#!/usr/bin/env python
#@Time     :2020-01-01 13:52:47
#@Author   :azhenglianxi

import itchat
import time
from itchat.content import *

d = r"D:\wq.png"
itchat.auto_login(hotReload=True)
itchat.auto_login(hotReload=True)
useinfo=itchat.search_chatrooms(name="甘泉三杰")
if len(useinfo)==0:
    print("没有找到群聊")
else:
    chatroomsname =useinfo[0]['UserName']
    print(useinfo[0]['UserName'])
    #itchat.send("@img@%s" % d, toUserName=chatroomsname)
    #for i in range(1,200):
    itchat.send("CP DD 不要笨蛋！请@离人的月亮",toUserName=chatroomsname)
    itchat.send_image("@img@%s"% d, toUserName=chatroomsname) # 发送照片有问题

    time.sleep(1)


