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
conn,addr =s.accept()


# 等待传入连接，在连接到之前会阻塞
# 连接成功之后 解除阻塞状态 并且返回一个新的套接字对象客户端的ip地址

print("k客户端的ip地址是：",addr)

# 接受数据
clien_data = conn.recv(1024).decode('utf8')
print(clien_data)

        # 发送数据
conn.sendall(input('请输入。。。').encode('utf8'))
conn.close()


s.close()