# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/4

import threading, time

se = threading.BoundedSemaphore(5) # 有五个停车位


def foo(num):
    se.acquire() # 停车位减一
    print("这是第几个", num)
    time.sleep(3)
    print("停车位释放")
    se.release() # 停车位加一

for i in range(20):
    t = threading.Thread(target=foo, args=[i])
    t.start()


