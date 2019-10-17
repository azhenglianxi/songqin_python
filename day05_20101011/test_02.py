# 求 1+2+……100
def get_sum(start, end, step=1):  # 必填形参 step =1 ----缺省参数-- 不传入就是默认值
    sumData = 0  # 结果和
    cnt = start  # 初始值
    while cnt <= end:
        # 条件满足下一只执行里面的代码
        sumData += cnt
        cnt += step  # 自变量加1
    return sumData


print(get_sum(2, 11, 2))

namelist = ['mike', 'jack', 'mary']
for i in namelist:
    print(i)
for j in range(2, 11, 2):  # # 需要写一个循环的次数 01234 左含右不含 --步长默认是1
    print(j)

# 4- break 跳出本层循环！
#     alist = ['Mike', 'Jack', 'Mary', 'Pat','Will','Lisa']
#     for one in range(0,2):# 2次  0  1
#         for name in alist:
#             print(name)
#             if name == 'Jack':
#                 break
# 5- continue --结束本次循环
#     1- 当continue的条件满足的时候，它后面的语句要执行吗？  -- 不要
#  3- 函数内容注释
#     def func():
#         'this is func doc'
#          print('函数！')
#          print(func.__doc__)
