# 字符串
# info = "name is tom" #<class 'str'>
# info = 'name is \' tom'#转义符
# print(type(info))

# 2.拼接--- 字符串只能与字符串的拼接
# 先入为主的  错误示范
# print("hello"+ 3) #can only concatenate str (not "int") to str 修改方案将3强转成str（）
# print(3+"sss") #unsupported operand type(s) for +: 'int' and 'str'

print("hello\n" * 3)  # \n 换行符 \r 回车符 \t 制表符

# 3 sequence 序列 正下标 从左到右 长度是len()-1
info1 = "name is tom"
print(len(info1))  # 回去元素的长度也是个数
print(info1[0])  # 取0的下表
print(info1[len(info1) - 1])  # 灵活性 确定一定要 数字的最后一个

# 3-2 附下标 从右边到左边 从-1 到len
# print(info1[-1])
# print(info1[-len(info1)])
# print(info1[11])   #下标越界 string index out of range

# 4 切片操作
print(info1.index("i"))  # 获取当前下标
print(info1[5:5 + 2])  # [5:5+2]切片范围 然后在+下标要回去的长度【左含右不含】
# 4-2 获取前半段--写后面一刀的下标--冒泡后面的位置
print(info1[:4])
print(info1[-3:])
print(info1[::-1])  # 切片操作【前一刀】下标 后一刀下标 倒叙

# 4-3 截取日志 左右两边都变化---不太适合用切片片操作字符串
# info1.split()
# import re  正则模块
