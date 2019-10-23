class Tiger:#创建类
    className =  '老虎'#静态属性--属于整个类--每一个个体都一样:调用：实例.属性  ；类.属性
    #初始化方法---本质：函数
    def __init__(self,inWeight=200):#只要创建实例，就会自动被调用
        self.weight = inWeight
    #1- 实例方法--函数---跟实例有关
    def roar(self):#self--不需要你操作--谁调用就是谁！
        print('wow!!!,体重减少5斤！')
        self.weight -= 5

    def feed(self,food):#实例方法
        if food == '肉':
            print('恭喜，喂食正确，体重增加10斤！')
            self.weight += 10
        else:
            print('抱歉，喂食错误，体重减少10斤！')
            self.weight -= 10

class Sheep:#羊
    className =  '羊'#静态属性--属于整个类--每一个个体都一样:调用：实例.属性  ；类.属性
    #初始化方法---本质：函数
    def __init__(self,inWeight=100):#只要创建实例，就会自动被调用
        self.weight = inWeight
    #1- 实例方法--函数---跟实例有关
    def roar(self):#self--不需要你操作--谁调用就是谁！
        print('mie!!!,体重减少5斤！')
        self.weight -= 5

    def feed(self,food):#实例方法
        if food == '草':
            print('恭喜，喂食正确，体重增加10斤！')
            self.weight += 10
        else:
            print('抱歉，喂食错误，体重减少10斤！')
            self.weight -= 10



class Room:
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal




#-------游戏初始化--创建10个房间实例----------
from random import randint#随机取整数
roomList = []#存放房间实例
for one in range(1,11):
    if randint(0,1) == 1:
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(one,ani)
    roomList.append(room)
#--------------------------------------
#--------------开始游戏-----------------
import time
#游戏的开始--定义一个开始时间
startTime = time.time()# 单位是 s

while True:
    curTime = time.time()#当前时间
    if curTime - startTime > 30:
        print('时间到了，游戏结束！')
        for one in roomList:#one---房间实例
            print('当前房间编号:{},动物是:{},体重是:{}斤'.format(one.num,one.animal.className,one.animal.weight))
        break
    #1- 随机弹出一个房间号
    roomNum = randint(1,10)#双闭----int--房间号而已
    roomObject = roomList[roomNum-1]#取房间实例
    #2- 提示用户
    answer = input('当前房间编号是:{},您是否需要敲门:(y/n)?'.format(roomNum)).strip()
    #3- 判断用户是否敲门：
    if answer == 'y':#敲门
        #这个房间的实例.动物.叫
        roomObject.animal.roar()
    #4- 喂食
    food = input('请投喂食物:(肉/草)?').strip()
    # 这个房间的实例.动物.吃
    roomObject.animal.feed(food)
