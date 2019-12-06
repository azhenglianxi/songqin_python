#!/usr/bin/env python
#@Time     :2019-12-06 20:39:42  
#@Author   :azhenglianxi   
import  socket ,os

def get_file(sk_obj,file_path):
    '''
    #
    :param sk_obj:  socker 对象
    :param file_path: 接受到的文件存路径
    :return:

    '''
# 接受文件大小
    file_size =int(sk_obj.recv(1024).decode('utf8'))
    sk_obj.sendall(b'ok')# 避免黏包 与另一端对应

    #接受文件名称：
    file_name =sk_obj.recv(1024).decode('utf8')
    sk_obj.sendall(b'ok')  # 避免黏包 与另一端对应

    # 接受文件正文
    with open("%s/%s" %(file_path,file_name),'w') as f :
        while file_size >0:
            f.write(sk_obj.recv(1024))
            file_size-=1024


sk=socket.socket()
# 向服务端发起连接
sk.connect(("127.0.0.1",13001)) # 元祖传参
# 接受数据
get_file(sk,'./ ')
sk.close()