# 函数的方法
# 1. count ---计算字符出现的次数
info = 'name is tom tom'
print(info.count('tom'))
if info.count('tom') != 0:
    print("存在！")
else:
    print("不存在！")
print(info.count('tom', 0, 12))  # 区域搜索
# 2. find 只能获取第一个下标
print(info.find('tom'))  # 查到出现的位置 返回的是正下标 如果查到的字符不存在 返回-1
info1 = 'adsdasdas'
idx = info.find('a')


# find 只能从定位开始查找 index不能
def my_find(instar, info1):  # 考虑 找到返回下标 要么返回-1 可以判断 他是一个if结构
    if instar in info1:
        return info1.index(instar)
    else:
        return -1


print(my_find('c', info1))

# #使用场景
# if str1.find('a') != -1:
#     print('存在！')


info1.isdigit()
# 判断纯数字 或者判断纯字母
info1.isalpha()  # 判断是不是纯字母
info1.isdigit()  # 判断是不是纯字母
info1.lower()  # 大写转小写
info1.upper()  # 小写转入大写
info1.strip()  # 删除左右两边的空格 中间的不能删除
print(info.replace('tom', 'tome'))  # 默认替换是全部

print('***'.join(['1', 'we', 'wewewd']))
print(info1.split(' '))  # 以切点去切 切点会被干掉 返回一个列表
print(str([1, 3]))
# 要想获取一段字符串里的某个字符 或者某一段 除了切片可以用split()
infop = 'A pretty boy come in, the name is Patrick, level 194'
print('sdasdas' + infop.split(",")[0].split(' ')[1])
