# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/12/4

import threading, time

account_balance = 500 # 账户余额
lockA = threading.Lock() # 声明一把锁 # 同步锁

# 操作账户余额
def option_balance(num):
    global account_balance # 申明全局变量

    lockA.acquire() # 上锁
    # 把变量存到自己的系统
    balance = account_balance
    time.sleep(1) # 省略一系列算法
    balance = balance + num

    # 将计算结果返回
    account_balance = balance
    lockA.release() # 解锁


# 支付宝里边的线程
t1 = threading.Thread(target=option_balance, args=(-300, ))
# 银行的线程
t2 = threading.Thread(target=option_balance, args=(10000, ))

t1.start() # 启动线程
t2.start() # 启动线程
t1.join()
t2.join()


print("所有线程执行完毕")
print("最终余额:", account_balance)

