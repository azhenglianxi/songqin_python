# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/4



import threading, time

# lock1 = threading.Lock() # 属于小明的锁 -- 同步锁
# lock2 = threading.Lock() # 属于面试官的锁 -- 同步锁

lockR = threading.RLock() # 递归锁

# 小明
def foo1():
    lockR.acquire() # 上锁
    print("请给我发offer")
    time.sleep(1)

    lockR.acquire() # 上锁
    print("解释什么是死锁")
    time.sleep(1)

    lockR.release() # 解锁
    lockR.release() # 解锁


# 面试官
def foo2():
    lockR.acquire() # 上锁
    print("请解释什么是死锁")
    time.sleep(1)

    lockR.acquire() # 上锁
    print("发offer")

    lockR.release() # 解锁
    lockR.release()  # 解锁


t1 = threading.Thread(target=foo1) # 小明
t2 = threading.Thread(target=foo2) # 面试官

t1.start()
t2.start()




