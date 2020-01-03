import itchat   # 微信个人消息

#产生二维码
itchat.auto_login(hotReload=True)
#定义用户的昵称
send_userid='1'
#查找用户的userid
itcaht_user_name = itchat.search_friends(name=send_userid)[0]['UserName']
#利用send_msg发送消息
f=r"D:\Program Files\Python_package\songqin_python\Selenium_auto\wq.png"
itchat.send("@img@%s" % f, toUserName=itcaht_user_name)

