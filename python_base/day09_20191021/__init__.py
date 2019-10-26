class Tiger:
    nickName = '老虎'#静态属性：每一个该类的实例都是一样的

    def __init__(self,inWeight=200):#当创建实例的时候，会自动调用   self不需要程序员传入的，就是实例本身
        self.weight = inWeight#实例属性---只能是实例去调用
    #
    #实例方法---叫  一般在类，默认是实例方法
    def roar(self):
        print('wow!!!---体重减5斤')
        self.weight -= 5

    #喂食
    def feed(self,food):
        if food == '肉':
            print('恭喜，喂食正确，体重增加10斤！')
            self.weight += 10
        else:
            print('抱歉，喂食错误，体重减少10斤！')
            self.weight -= 10




#2- 定义羊类
class Sheep:
    nickName = '羊'  # 静态属性：每一个该类的实例都是一样的

    def __init__(self, inWeight=100):  # 当创建实例的时候，会自动调用   self不需要程序员传入的，就是实例本身
        self.weight = inWeight  # 实例属性---只能是实例去调用

    #
    # 实例方法---叫  一般在类，默认是实例方法
    def roar(self):
        print('mie!!!---体重减5斤')
        self.weight -= 5

    # 喂食
    def feed(self, food):
        if food == '草':
            print('恭喜，喂食正确，体重增加10斤！')
            self.weight += 10
        else:
            print('抱歉，喂食错误，体重减少10斤！')
            self.weight -= 10


#3- 定义房间类  有2个属性  编号 动物
class Room:
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal

#----------游戏初始化----创建10个房间的实例---------
from random import randint
roomList = []#10房间的实例
for cnt in range(1,11):#1---10
    if randint(0,1) == 1:
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(cnt,ani)#房间实例
    roomList.append(room)
#-------------------------------------------------
import time
startTime = time.time()#开始时间
#---------------------开始游戏---操作
while True:
    curTime = time.time()
    if curTime-startTime > 30:
        print('时间到，游戏结束！')
        for one in roomList:#one----房间实例
            print(f'第 {one.num} 号房间,动物是:{one.animal.nickName},体重是:{one.animal.weight};')
        break


    #游戏逻辑
    roomNum = randint(1,10)
    roomObject = roomList[roomNum-1]#列表有10个下标是 0 9 房间实例
    print('当前房间编号是:{}'.format(roomNum))
    #2- 提示 & 接收 用户是否敲门操作21：10
    answer = input('是否选择敲门(y/n)?').strip()
    #3- 判断是否要敲门操作
    if answer == 'y':
        roomObject.animal.roar()#房间里的.动物.叫操作

    #4- 喂食
    food =  input('请输入投喂的食物:(肉/草)?').strip()
    roomObject.animal.feed(food)
