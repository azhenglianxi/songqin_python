#!/usr/bin/env python
#@Time     :2019-12-03 17:09:17  
#@Author   :azhenglianxi   
import time
def boot_mation(username):
    def bar(func):
        def inner(somthing):
            func(somthing)
            # 此处省略一系列神仙操作
            print("成功利用摄像头捕捉到用户视网膜映射的手机壳颜色")
            print("成功调整 UI 界面主题")
        return inner
    return bar


user='张三'
@boot_mation(user)
def foo(somthing):
    # 此处省略一连串函数调用
    time.sleep(1)
    # 此处省略一连串🐂🍺算法
    print('do somthing',somthing)
foo('wee')


