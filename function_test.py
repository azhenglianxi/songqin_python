def func():  # 函数的定义--不会执行里面的任何代码--用意：告诉python 解释器 这是个函数 名字
    pass


func()  # 函数调用才会运行里面的代码


def get_sum(a, b):  # 形参 在函数定义地方--形式主义
    # print(a+b)
    return a, b, a + b  # 谁调用给谁
    print(1)


get_sum(1, 3)  # 实参 在函数调用的时候 ,实际传入的值
# get_sum(b= 'hello',a=2)
# get_sum('hello',b=2)
# get_sum(a ='hello',2) #函数调用的时候，一旦出了变量 =值 写法，后面的参数要保持队形

# 函数的返回值**** 可以返回一个数组 然后再用切片的方式回去数据
# 一个函数只有一个返回值  可以在if里写不同的返回值
res = get_sum(10, 20)
print(res[0:2])
# def unreachable(a,b):
#     if a>b :
#         return a
#     elif a<b:
#         return b
# print(unreachable())

# 1-str() --转化成字符串类型
# round(小数，位数精度)

name = 'sss'
age = '132'
print('%s %s' % (name, age))
infoo = f'我叫{name:0<6},年龄是{age}'
print(infoo)

name = 'tom'
data = f"{{'name':{name}}}"
data1 = "{'name':%s}" % name

print(type(data))
print(data1)

# 大括号之内还可以再嵌套
s1 = input('输入要填充的符号')
print('{:{s}^10.2f}'.format(1.12345, s=s1))
# @@@1.12@@@


# 循环
