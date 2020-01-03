#!/usr/bin/env python
#@Time     :2020-01-01 13:52:47  
#@Author   :azhenglianxi   

import itchat
import time
from itchat.content import *

sum =0
itchat.auto_login(hotReload=True)
useinfo=itchat.search_chatrooms(name="甘泉三杰")
if len(useinfo)==0:
    print("没有找到群聊")
else:
    #chatroomsname =useinfo[0]['UserName']
    itchat.send("1",useinfo)
    time.sleep(1)
# gname = '甘泉三杰'
#
# context = '121212'
# def SendchatRoomsMsg(gname,context):
#     myroom =itchat.get_chatrooms(update=True)
#     global username
#     mps = itchat.get_mps()
#     friends = itchat.get_friends()
#    # chatrooms = itchat.get_chatrooms()
#     #contact = itchat.get_contact()
#     print(mps,friends)
#
#     #搜索群名
#     myroom =itchat.search_chatrooms(name=gname)
#     for room in myroom:
#         if room['NickName']==gname:
#             username=room['UserName']
#             """
#              如果单纯的使用send函数，需要对发送内容进行标注。
#         @fil@：在发送内容前添加，表明是发送文件
#         @img@：在发送内容前添加，表明是图片文件
#         @msg@：在发送内容前添加，表明是消息
#         @vid@：在发送内容前添加，表明是视频文件，视频文件要小于20M
#         如果什么都没有添加，默认是消息
#
#             ithcat.send("@fil@%s" % '/tmp/test.text')
#             ithcat.send("@img@%s" % '/tmp/test.png')
#             ithcat.send("@vid@%s" % '/tmp/test.mkv')
#             """
#             itchat.send("@img@%s" % 'D:\\wq.png',toUserName=username)
#         else:
#             print("No groups found")
#
# #@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True,isMpChat=True)
# #def text_reply(msg):
#    #  print(msg)
#
# itchat.auto_login(hotReload=True)
# SendchatRoomsMsg(gname, context)
# itchat.run()


