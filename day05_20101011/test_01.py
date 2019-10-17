# 字符串格式化
name = 'tom'
height = '123'
print('我叫%s''身高是%s' % (name, height))  # 2个元素以上需要同元祖形式展示
# %S
# %d
# %f
# %x
print('%-6.3f' % 3.1415926)  # 字符串格式化输出小数点后 6位
# #1-    长度d%  长度值是正数---右对齐，左补齐     负数：左对齐，右补齐
# 小数处理
print('%2.f' % 3.1415926)  # 格式化输出默认是6位 --四舍五入

# 2.字符串方法  ----format
# name = 'tom'
# age = 20
# #1- 顺序填值  >   右边--右对齐  < 左对齐   ^中间对齐
# # info = '我叫:{:0>6},年龄是:{:*>6}'.format(name,age)


info = '我叫{:<5},年龄{:<5}'.format(name, height)  # {:<5} 左对齐 五格间距

# 2.下标填值
# info = '我叫{1:5},年龄是{0:>5}'.format(name,height)
print('111111' + info)

name = 'tom'
data = f"{{'name':{name}}}"
data1 = "{'name':%s}" % name
print(data)
print(data1)
