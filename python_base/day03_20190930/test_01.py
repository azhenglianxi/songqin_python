# 布尔表达式（布尔类型）
# == ！= > < >= <= 都是比较操作符号
#

# 2-1 数值比较1.比较值是否相等 2.比较地址是否相等（是否是同一个对象）
# print(20 != 10)

# 2-2 字符串比较 --比较对应未知的字符的ascii
print('abcd' > 'b')
# 字符串 in 和 not 前面是后面的一个字符 ：前面是后面的连续
# 应用场景： 做检查点  页面是跳转成功 判断用户是不是登录成功的
str1 = 'adsasdasdasd'
print('a' not in str1)

# 列表的 in 要为真： 前者是后者的一个元素
alist = [10, 20, 30]
print([10, 20] in alist)
print(10, 20 in alist)

# 3 条件组合
# 3-1 且：全真为真，一假为假 ---
# 条件1 为假，条件根本不会执行
print(3 > 1 and 2 == 1)
#  3-2 或：一真为真 全假 为假


# 没有括号的情况下   not  > and  > or
# （3(2(1))） 从里往外

# 4 -扩展   复制 就是引用(指向) ---是同一个对象
# alist1 =[10,20,[100,200]]
# # blist = alist1
# # # 对A列表进行操作
# # alist1.append(55)
# # print('a列表',alist1)
# # print('b列表',blist)

# 4-2 浅拷贝-- 外列表不是同一个对象 内列表是指向同一个的

# 用途;对于列表用的比较多
# import copy
# alist2 =[10,20,[100,200]]
# blist1= copy.copy(alist2)
# #下面对A 进行操作
# alist.append("a列表",alist2)
# print('a列表',alist2)
# print('b列表',blist1)

# 4-3 深拷贝-- 列表不是同一个对象
import copy

alist2 = [10, 20, [100, 200]]
blist1 = copy.deepcopy(alist2)
# 下面对A 进行操作
alist.append("a列表", alist2)
print('a列表', alist2)
print('b列表', blist1)
