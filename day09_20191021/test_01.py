#面向对象 类和实例
class Tiger():
    nickName='老虎' #静态属性---统称--术语:属性 俗称：特征 本质是：变量、

    def __init__(self,inweight=200): #初始化构造函数 当创建实例的时候 他一定会被调用 本质：函数
        self.weight =inweight    # self 是参数 不需要程序员自己填，解释器会自动传入
        print('老虎父类初始化方法')
    # 实例方法 ********** 老虎的实例方法***********
    #
    def roar(self):  #叫声方法
        print('wow!,体重减少五斤！')
        self.weight -=5

    def feed(self,food):  # 喂食的方法
        if food=='meat':
            print('恭喜喂食正确，体重增加十公斤！')
            self.weight +=10
        else:
            print('抱歉，喂食错误，体重减少10公斤！')
            self.weight-=10

    #静态方法  (如果代码中的实例方法不访问任何实例属性，一般建议实现为静态方法)
    @staticmethod  #静态装饰器
    def static_roar():
        print('只是简单的叫一声')


class Sheep():
    nickName ='sheep'
    def __init__(self,inweight=100):
        self.weight =inweight
    def roar(self): #叫声方法
        print('mie~~')
        self.weight-=5
    def feed(self,food): # 羊吃的方法
        if  food =='grass':
            print('恭喜你 喂食成功')
            self.weight +=10
        else:
            print('抱歉，喂食错误 投食减少10公斤')
            self.weight -=10
    #创建一个房间类 实例化
class Room:
    #初始化这个类
    def __init__(self,Num,Animal):
        self.Num =Num
        self.Animal =Animal


# #创建实例
# t1=Tiger()
#
# #房间实例
# r1 =Room(1,t1)
# -----------游戏初始化创建10 房间实例  随机分配-------------
from random import randint

roomList =[]
for i in range(1,10): #通过偏离1-10 来确定是个放假
    if randint(0,1)==1:  #通过随机数来指定 0：老虎 1：羊
        ani=Tiger(200)
    else:
        ani=Sheep(100)
    room =Room(i,ani)#(i,'动物')
    roomList.append(room)


# --------------- 游戏限时，直接到游戏结束-------------
import time

#游戏的开始 --定义
startTime =time.time()
while True:
    curTime =time.time()
    atime =curTime-startTime
    if atime > 120:
        print('\n\n ***********游戏结束*******\n\n')

        for idx,room in enumerate(roomList):
            print('房间：%s' %(idx+1),room.Num.nickName,room.Animal.inweight)
            break
    roomno = randint(1, 10)
    room = roomList[roomno - 1]  # why -1 ?
    ch = input('我们来到了房间# %s, 要敲门吗?[y/n]' % roomno)
    if ch == 'y':
        room.Animal.roar()

    food = input('请给房间里面的动物喂食:')
    room.Animal.feed(food.strip())








