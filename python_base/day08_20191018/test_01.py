'''
1-模块的概念：---试卷
    一个.py文件就称之为一个模块（Module）
2-包的概念：---试卷夹
    这些组织存放模块文件的目录，我们称之为包(Package)
3-模块与包的优势：
    1-方便别人调用
    2-避免同名变量/函数
    3-每个模块中的变量名作用域只在本模块中
4-模块的使用：
    1-同一个包内的调用：
        1- import 模块名--- 相当于执行了一遍导入的模块
        2-使用变量/函数：import后面的内容 . 函数/变量
        3-如果我们模块名很长---as  取别名
            1-优势：可以减少字符长度   
            2-避免同时导入2个/多个模块里面有同名函数,出现覆盖情况
        4-from 模块名 import 函数/变量
            from  mathFunction import sumFunNew
            sumFunNew(1,2)
         导入全部：from mathFunction import * ===  import   mathFunction
        优势：可以节省字符长度描述
        劣势：导一个用一个，如果还有需求，增加下
    区别： 
        1- import xx---全部导入
        2- from 模块 import 函数/变量 ,指定内容导入，如果后期有增加的话，再增加imnport后面的内容
    2-不同包的调用：
        1-import testP.pTest  testP.pTest.func()
    3-__init__.py模块：
        1-初始化模块
        2-只要你调用这个包，那么该包的__init__.py，就会被执行！
5-标准库的使用：
    1-不需要程序员去 import---直接使用变量和函数---print / open  /len
    2-import time
      print(time.strftime("%Y_%m_%d %H:%M:%S"))
    3- 标准库
        1- 内置类型& 内置函数--直接使用-不需要import
        2- 内置模块--要使用import
        案例：
            from  datetime import date
            now = date.today()
            print(now)
6-模块搜索规则：
    1-import sys----sys.path
    2- sys.path---第一个是空地址----当前目录 
7-增加路径：
    1-import sys---临时的
        sys.path.append('g:/file')
    2-cmd--set PYTHONPATH=g:/file
'''

'''
1- import
    1- 在同一包内
        1-  import 模块名 
        2- 函数的调用： 模块名.函数()
    2- 不同包内：
        1- import 包1.包2.模块名
        2- 函数的调用：包1.包2.模块名.函数()
    3- 起别名-- as
        import 包1.包2.模块名 as 名字
        名字.函数()
    使用场景：
        1- 如果需要导入整个模块
        2- 不清楚需要具体导入某一个函数
        
2- from  xxx   import xxx
    1- 在同一包内
        1- from  模块名 import 函数
        2- 函数的调用：函数()
        注意事项：导一个有一个
    2- 不同包内：
        1-  from 包1.包2.模块名 import 函数
        2- 函数的调用：函数()
    3- 起别名-- as
        from 包1.包2.模块名 import 函数 as 别名
        别名()
        作用：
            1- 减少输入字符长度
            2- 避免导入对象的冲突--区分
    4- 全部导入：
        from xxx import *---不太建议

'''

#import 同一个包
# import mathFunction
# mathFunction.sumFun(1,2)

#import 不同一个包

# import moudleTest.mTest as mt#起别名
# mt.test()

#2- from import--具体&明确需要哪些---
# from mathFunction import sumFun
# from moudleTest.mTest import sumFun as mt
# sumFun(1,2)#不需要任何前缀
# mt(1,2)
# import moudleTest

# import mathFunction

#1- __name__  每一个模块都有属性---在当前模块运行的时候，当前模块的__name__ = '__main__'
#2- 当一个模块被调用，那么他的__name__的值就是他自己的模块名

# print(__name__)
# import mathFunction


# print(time.strftime("%Y_%m_%d %H:%M:%S"))

import sys
print(sys.path)
sys.path.append('G:\\')#人为增加--这个是需要解释器执行代码才生效-临时性
#import xintian#如果import 导入模块报错，为控制台输出结果为准
#报错机制--是pycharm
#xintian.test()


# print('****begin  mathFunction!****')
version = 0.1
buildData = '2018.02.08'

def sumFun(a, b):#定义
    print('%d + %d = %d'% (a,b,a+b))
def difFun(a,b):#定义
    print('%d - % d = %d' % (a,b,a-b))

# print('****end  mathFunction!****')





if __name__ == '__main__':#可以写一些本模块调试代码，内部不想给调用的代码
    #注意事项：当我们点击：if __name__ == '__main__': 从这个模块的第一行代码，开始运行
    sumFun(1, 2)
    difFun(1, 2)

