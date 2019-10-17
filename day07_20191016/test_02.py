# 函数的作用域

# 全局变量
# 局部变量

#1缺省 参数 --为了函数被调用 传入实际值 则以实际值为准 没有 已缺省为准
def fun(a,b=2):
    print(a,b)
fun(1)
# 2. 可变数量参数 参数顺序（必填，可变数量，可缺省）
def func(a,*b,c=4):  #在函数定义是 * 代表可变参数 代表0--n 会封装一个元祖类型
    print(a,b,c)
func(1,2,3,4,5)


#  3. 关键字可变数量参   封装成一个子字典   如果把形参转化成字典的化
def funcc(a, **kwargs):
    print(a,kwargs)
funcc(1,name='tom',age=20)