#!/usr/bin/env python
#@Time     :2019-12-03 10:34:23  
#@Author   :azhenglianxi

# 1.函数名可作为参数传递
# def bar(a):
#     print('bar')
#     a()
# def foo():
#     print('foo')
#
#
# bar(foo)

# 2、函数名可以赋值给其他变量
# def foo():
#     print('foo')
#     return bar
# def bar():
#     print('bar')
# b=foo()
# b()

#
# def login(usr):
#     if usr == 'xs':
#         return True
#
#
#
# def wrapper(funcname):
#     if login('xs'):
#         return funcname

#
# def home():
#     print('this is the home page!')
#
# home = wrapper(home)
# home()

def Before(request):
    print( 'before')

def After(request):
    print( 'after')

# def Filter(before_func,after_func):
#     def outer(main_func):
#         def wrapper(request):
#             before_result = before_func(request)
#             if(before_result != None):
#                 return before_result;
#             main_result = main_func(request)
#             if(main_result != None):
#                 return main_result;
#             after_result = after_func(request)
#             if(after_result != None):
#                 return after_result;
#         return wrapper
#     return outer
#
# @Filter(Before, After)
# def Index(request):
#     print('index')

#Index('example')



# 只会向外寻找而不会向内寻找 故P报错

# def foo():
#     a ='hellow,world'
#     def bar():
#         b='hellow,world'
#         print(a)
#     print(b)
# foo()
#
# def outer():
#    x = 10
#    def inner():
#       print(x)
#    return inner
# # 我现在想调用 inner 函数,怎么办?
# outer()()
































