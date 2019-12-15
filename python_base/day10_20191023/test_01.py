#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time     :2019-10-23 21:16:58
#@Author   :azhenglianxi
#@Site     :
#@File     :test_01.robot
#@Software :PyCharm

#异常处理
#if----过滤---过滤已知 前置
#try except  -- 后置

#针对 可能出现的异常 进行处理
import traceback
# while True:
#     num =input('input a nimber')
#     try:
#         print('100 /%s =%s' %(num,100.0 /int(num)))
#     except ZeroDivisionError:   #捕获一种异常 ---已知异常
#         print('你输入的值为 0，重新输入')
#     except ValueError as err: # 用于打印这个错误  差生的异常 吧处理的异常写入日志
#         print('------请输入数值------')
#     except Exception:  # 捕获所以异常
#         print('异常了')
#     except:  # 日志信息 返回值 打印 所以 错误
#         print('处理异常----',traceback.format_exc())
# #
# 1- 工具：点开工具--会指定路径去打开文件-------文件不存在会报错  ---加异常机制
# 2- web ui  --selenium--
#     1- 10个用例执行第3个用例的时候--元素定位失败会怎么样？---代码会停止--报错
#     2- 效率低
#     3- 改善：加异常机制：3出错--12  45678910都会执行--
#     4- 可以针对性去排除哪个用例的颜色定位问题


#自定义异常处理(继承异常普通类)
#class NAMEerro(Exception):
#    pass

for i in range(1,5):
     if i ==3:
         raise  ValueError  #raise 抛出异常
# 断言 assert---检查点-----如果后续代码比较重要，而且很依靠前面的数据或者状态
tel = input('请输入手机号：')
assert len(tel) == 11,'手机位数有误！'
# print('我在处理手机运营商操作')
# # #--对手机号进行供应商鉴别
