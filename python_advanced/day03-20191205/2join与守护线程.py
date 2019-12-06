# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/4
import threading, time

def foo(num, something):
    for i in range(num):
        print("CPU切换执行", something)
        time.sleep(1)

# 创建线程对象
t1 = threading.Thread(target= foo, args=[5, "看电影"])
t2 = threading.Thread(target= foo, args=(10, "听音乐"))

t1.setDaemon(True) # 申明守护线程
t2.setDaemon(True) # 申明守护线程

t1.start() # 启动线程
t2.start() # 启动另一个线程


# # t1.join() # 阻塞主线程， 在调用join方法的线程实例运行结束之前， 一直阻塞
# # t2.join() # 阻塞主线程， 在调用join方法的线程实例运行结束之前， 一直阻塞
# for i in range(10):
#     print("这是主线程")
#     time.sleep(1)

print("over")
