# 列表有元祖（元素的个数可以改变 元素的值可以改变）
alist = ['10', '3.14', 'hello', [100, 200]]
# 1-1 获取列表元素---下标 最快
# print(alist[0])
# 1-2 切片
# print(alist[:1]) #列表切完还是列表
# 1-3 常用操作
# print(len(alist))
# print(100 in alist[len(alist)-1])
# print(alist[-1][0])
# alist[-1].append(5) #在尾部插入
# alist[-1].insert(0,['a','b']) #(需要插入的下标位置，插入的值)
# alist.insert(100,55)#如果insert 插入的下标大于len, 不会越界，相当于append
# print(alist)
# 1-3-2:删除元素
# del ---对列表的下标操作
# del alist[-1],alist[2]  #删除中间数据之后 下标会变 进行重新排列
# del alist[1:1+2]# 删除中间元素
# del alist[::2]跳着删除   2 把步子判断步调
# alist.remove(100)
# while 10 in alist:   #删除列表里重复的数据 循环结束
#    alist.remove(10)
# 元祖
# 定义元祖一定要到
tuple1 = (1,)
print(type(tuple1))
# 类型转换--元祖 原对象不改变 是新对象另存的新地址
alist = [10, 20]
a = tuple(alist)

print(type(a))
