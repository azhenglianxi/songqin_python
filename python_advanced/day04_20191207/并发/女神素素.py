#!/usr/bin/env python
#@Time     :2019-12-06 22:32:59  
#@Author   :azhenglianxi   

import socketserver
class myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("有人和女神搭讪。。。")
        while True:
            # 接受数据
            client_data=self.request.recv(1024).decode('utf8')    # conn.recv
            if client_data =='exit':break
            print("客户端：", client_data)

            # 发送数据
            self.request.sendall(input("请输入。。").encode('utf8'))    #conn.sendall
        self.request.close()

se =socketserver.ThreadingTCPServer(("127.0.0.1",13003),myserver)
print("女神上线了")
se.serve_forever()
print(23)