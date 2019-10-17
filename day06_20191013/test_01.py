# 文件的读写方式
# win 的换行--\r \n 2个长度 ’\n'-- 一个
# xpath 叫相对路程 h和绝对路径
fileDir = 'd:/1.txt'
fileDir2 = 'g:\\n 1.txt'  # 错误写法 一般都\\n
fileDir3 = r'g:\n 1.txt'  # r---取消转义
# 从别的地方获取文件
fileDir4 = repr(fileDir3)  # repr
file_object = open()  # 默认模式是R
fileDir = r'g:\1.txt'
fo = open(fileDir)  # 读文件操作
print(fo.tell())  # 文件最开始的指针---0
print(fo.read(2))  # 读取具体的个数
fo.seek(1, 0)  # (位置，模式)0 模式--从0开始算的--跟r 模式操作文件搭配
print(fo.tell())  # 最开始文件指定的位置 ---2  指定文件读取的位置

"""
abcd
1234
seek 1. （1,模式）----0 模式 --绝对位置 从0开始--配套 ’r'
      处理：文本文件-txt ,log ---返回 -str 
    2. （1，模式）---1模式 --当前位置，开始
    文件打开模式一定是rb-- 读取二进制（bin） pacp 格式 图片 音频视频
    1- 0模式---绝对位置模式   fo.seek(1,0)
            前提：python3 一定在'rb'模式下---二进制模式--非文本文件(图片)
    2- 1模式---当前位置开始移动 fo.seek(移动的位数,模式1)
                    移动的位数 正数：向后移   负数：向前移

    3- 2模式---从尾部
       1- fo.seek(-1,2) 
       2- 移动的位数 正数：向后移   负数：向前移

"""
# 8 - readline读取一行
# 1 - 该方法返回是
# 1 - 该方法返回是
# print(type(fo.readline())) - - <class 'str'>
#
#
# 2 - 文件指针会做相应的偏移
#
# 9 - readlines读取所有行
# 1 - 该方法返回是
# print(type(fo.readlines())) - -
#
#
# 区别：
fo.read()  # - ---返回str
fo.readlines()  # - --返回是list - --每一行是里面一个元素！
fo.read().splitlines()  # - --返回list 而且去掉换行符
#
