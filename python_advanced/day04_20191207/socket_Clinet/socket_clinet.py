#!/usr/bin/env python
#@Time     :2019-12-06 20:39:42  
#@Author   :azhenglianxi   
import  socket
sk=socket.socket()

# 向服务端发起连接
sk.connect(("127.0.0.1",13000)) # 元祖传参

while True:
    # 发送数据
    my_inp=input("请输入》》》")
    sk.sendall(my_inp).encode('utf8')
    if client_data =="exit":break


    # 接受数据
    server_data=sk.recv(1024).decode('utf8')
    print("服务端",server_data)
# 发送 数据
sk.close()