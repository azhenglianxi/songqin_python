#面向对象 类和实例
class Tiger():
    nickName='老虎' # 静态属性---统称--术语:属性 俗称：特征 本质是：变量、

    def __init__(self,inweight=200): # 初始化构造函数 当创建实例的时候 他一定会被调用 本质：函数
        self.weight =inweight    # self 是参数 不需要程序员自己填，解释器会自动传入
       #  print('老虎父类初始化方法')
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

    # 静态方法  (如果代码中的实例方法不访问任何实例属性，一般建议实现为静态方法)
 # @staticmethod  #静态装饰器
 #   def static_roar():
 #       print('只是简单的叫一声')


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
    # 创建一个房间类 实例化
class Room:
    # 初始化这个类
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
for i in range(1,11): # 通过偏离1-10 来确定是个放假
    if randint(0,1)==1:  # 通过随机数来指定 0：老虎 1：羊
        ani=Tiger(200)
    else:
        ani=Sheep(100)
    room =Room(i,ani)# (i,'动物')
    roomList.append(room)


# --------------- 游戏限时，直接到游戏结束-------------
import time

# 游戏的开始 --定义
startTime =time.time()
while True:
    curTime =time.time()
    atime =curTime-startTime
    if atime > 20:
        print('\n\n ***********游戏结束*******\n\n')
        # 重构for 循环下面的数据
        for one in roomList:
            print(f"第{one.Num}号房间，动物是{one.Animal.nickName},体重是:{one.Animal.weight}")
        break
        # 游戏逻辑
    roomNum = randint(1,10)
    roomObject = roomList[roomNum-1] # 列表有10个下标 0,9房间实例
    print('当前房间的编号是：{}'.format(roomNum))
    # 2.--提示 & 接受 用户是否敲门操作21:10
    answer = input('是否选择敲门(y/n)?').strip()
    # 3--判断是否要敲门操作
    if answer =='y':
        roomObject.Animal.roar()# 房间里的.动物.叫操作
    # 4--喂食
    food =input('请输入投喂的食物：（meat/grass）?').strip()
    roomObject.Animal.feed(food)
