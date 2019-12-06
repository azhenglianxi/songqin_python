#!/usr/bin/env python
#@Time     :2019-12-06 20:39:30  
#@Author   :azhenglianxi   


import socket

s=socket.socket()
# 为socket对象绑定ip
# 绑定IP 地址和端口号
s.bind(("127.0.0.1",13000))

# 监听有没有连接起来
s.listen()
print("女神空闲----------")
while True:
    conn,addr =s.accept()
    print("k客户端的ip地址是：",addr)
    while True:
        # 接受数据
        clien_data = conn.recv(1024).decode('utf8')
        if clien_data =='exit':break
        print("客户端说：",clien_data)

        # 发送数据
        conn.sendall(input('请输入。。。').encode('utf8'))
    conn.close()
    s.close()