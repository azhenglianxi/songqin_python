# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/4

import threading, time


begin_time = time.time()

# def foo(something): # I/O密集型任务，有等待
#     print("cpu正在执行", something)
#     time.sleep(1)
#
# """
# # 串行
# foo("写100M数据进入磁盘")
# foo("去做其他事情")
# end_time = time.time()
# print("总计执行时间:", end_time-begin_time)
# """
#
# # 并发
# t1 = threading.Thread(target=foo, args=("写100M数据进入磁盘", ))
# t2 = threading.Thread(target=foo, args=("去做其他事情", ))
#
# t1.start()
# t2.start()
# t1.join() # 阻塞主线程
# t2.join() # 阻塞主线程
#
# end_time = time.time()
# print("总计执行时间:", end_time-begin_time)



def bar(): # CPU密集型任务，计算密集型
    num = 0
    for i in range(10000000):
        num += 1
# # 串行
# bar()
# bar()
# end_time = time.time()
# print("总计执行时间:", end_time-begin_time)


t1 = threading.Thread(target=bar)
t2 = threading.Thread(target=bar)
t1.start()
t2.start()
t1.join() # 阻塞主线程
t2.join() # 阻塞主线程
end_time = time.time()
print("总计执行时间:", end_time-begin_time)


