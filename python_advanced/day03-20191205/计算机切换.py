#!/usr/bin/env python
#@Time     :2019-12-06 17:04:22  
#@Author   :azhenglianxi   


import threading,time
def foo(num,something):
    for i in range(num):
        print("cpu切换执行",something)
        time.sleep()
    t1 =threading.Thread(target=foo,args=[5,'看电影'])