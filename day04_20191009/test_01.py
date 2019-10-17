# 1.函数的定义
def func():  # 函数的定义--- 不会执行函数里面的代码
    print("step1")
    print("step2")
    print("step3")


func()  # 函数的调用---执行函数里的代码


# 自定义的函数 要自己先定义才能用

# 2.  形参 和  实参  形参是函数在调用使得参数  室参是实际传入的参数
def get_sum(a, b):  # a,b叫必填 形参--
    print(a * b)
    return a * b  # 一个函数的结束  --- 同一个锁紧后面不能写代码


get_sum(2, 3)  # 函数调用 实际传入参数的值

# 3. None ---没有返回值
#  函数的返回值的意义 ：函数的结果不一定要打印，要获取这个函数的记过的时候 需要函数运行后 返回值
res = get_sum(10, 20) + 5  # 返回值是多个对象的是，该返回元祖
# 总结： 得到函数的返回值是一个对象
# return 后面可以返回多个对象 但是函数调用者得到的是一个对象
# def unreachable(a,b):
#     if a>b :
#         return a
#     elif a<b:
#         return b
# print(unreachable())

# 类型转化
# str int  float
a = [10, 20]
print(type(a))
a = '100'  # int('字符串')--一定是整形的字符串数字
print(int(a))
print(float(a))
soctr = input("请输入分数:", '\n')
print(type(soctr))
print(int(soctr) + 20)

a = [10, 20]
b = str(a)  # "[10,20]"
