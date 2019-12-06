#!/usr/bin/env python
#@Time     :2019-12-06 20:39:30  
#@Author   :azhenglianxi   


import socket,os
def post_file(sk_obj,file_path):
    """
    用来发送一个文件
    :param sk_obj: socker 对象
    :param path: 需要传输的文件路径
    :return:
    """
    #发送文件大小
    file_size =os.stat(file_path).st_size
    sk_obj.sendall(str(file_size).encode('utf8'))

    sk_obj.recv(1024) #避免黏包

     # 发送文件名称
    sk_obj.sendall(os.path.split((file_path)[1].encode('utf8')))
    sk_obj.recv(1024)  # 避免黏包

    # 发送文件正文

    with open(file_path,'rb') as file:
        while file_size >0:
            sk_obj.sendall(file.read(1024))
            file_size-=1024   # 避免死循环 保证系统正常运行





s=socket.socket()
# 为socket对象绑定ip
# 绑定IP 地址和端口号
s.bind(("127.0.0.1",13001))
# 监听有没有连接起来
s.listen()
# 等待传入连接，在连接到之前会阻塞
# 连接成功之后 解除阻塞状态 并且返回一个新的套接字对象客户端的ip地址
conn,addr=s.accept()
# 发送数据
post_file(conn,"路径")
conn.close()
s.close()