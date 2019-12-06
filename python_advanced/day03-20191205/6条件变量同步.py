# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/4


import threading, time

num_list = [] # 存放包子
lock_con = threading.Condition() # 条件锁对象


# 消费者
def consumer():
    global num_list # 声明引用全局变量
    while True: # 不停的吃包子
        lock_con.acquire() # 上锁
        if len(num_list) == 0:
            print("没有包子吃")
            # 线程进入等待池
            lock_con.wait()
        else: # 有包子吃
            num_list.remove(num_list[0]) # 吃掉一个包子
            print("消费者吃掉了一个包子", num_list)
            time.sleep(1)
            lock_con.notifyAll() # 通知所有人来吃包子
            lock_con.release() # 释放锁
# 生产者
def producer():
    global num_list  # 声明引用全局变量
    while True: # 不停的生产包子
        lock_con.acquire() # 上锁
        num_list.append(1) # 往列表里边加一个元素
        print("生产者生产了一个包子", num_list)
        lock_con.notifyAll() # 通知所有人来吃包子
        time.sleep(1)
        lock_con.release()


t1 = threading.Thread(target=consumer) # 创建线程对象，消费者
t2 = threading.Thread(target=producer) # 创建线程对象，生产者
t1.start()
t2.start()



