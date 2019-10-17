# 字典
namelist=[#学生列表
   ['mike',25,180,80]
    ['tom',22,170,80]
]
def user_del ():
    del namelist[1]
user_del()
print(namelist[1][1])#  表达不清晰 下标容易发生变化 导致错误
 #2.字典的定义
dict1= {'name':'12312',(10,):10} # 字典
print(len(dict1))
print(dict1)
#特性：
# 1.键： 可以使int float tuple bool str --建议用
# 2.不可以是 list dictionary
# 3.值是任意值
# 4.键 对值 成对出现
#5. 字典没有下标
students ={
    'mike green':{
        'age':180,
        'height':111,
        'weight':15,
        'nicknam':'sss'
    }
}
print(students['tom']['age'])
dict2 ={'name':'tom','age':20}  # 键 ：值是唯一的
#1. 查询操作 用键去获取值
print(dict2['name01'])
#2. 修改值          先判断键 值存不存在
dict2['name']=1212
print(dict2)
#3. 用in 判断键值 存不存在
print('name'in dict2)
#4.字典 删除 没有 remove
dict2.pop()
del dict2
#5 .清空字典
dict2.clear()
# 6. 赋值 dict1 ={}
#7.获取key 返回的是 类列表 1.不支持下标取值 2.可以支持遍历操作
dict2.keys()
# 强制转化成list 回去下标
#8.获取所有的value

dict2.values()
 #9.获取所以的键对值
for item in dict2:
     pass
# 12 字典的合并
dict1.update('12')
# 出来键 跟值
for one in dict1:
     print(one,dict1[one])









#3.

