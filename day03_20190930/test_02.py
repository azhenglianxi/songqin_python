# 条件判断语句
# 1 选择分支机构
# if 条件判断  if语句  if-else语句 if-else if  if嵌套语句
# 单 if   语句--场景： 只需要对条件满足的处理，不满足的不需要单独处理
score = 80
if score > 60:
    # pass #空语句 避免语法报错
    print("及格！")  # 编程规范建是tab 四个空格

# 2 --if else 场景  满足 与不满足的情况各自都需要处理
score1 = 80
if score > 60:
    print("及格")
else:
    print("好好加油")

# 3--if elif  场景  当1 选择情况>2种以上
score2 = 80
if score2 >= 90:
    print("a")
elif score2 < 90:
    print("好好加油")
elif score2 > 80:
    print("好好加油")
print("run over1")

# 扩展 #只要if 后面跟着得是非零数据、非空字符串  非空列表 就是真
if 1:
    print('条件满足')
from random import randint

if randint(0, 10):  # 只要if 后面跟的是非零数值
    print("随机数取得--1")
else:
    print("随机数取得--0")

# 4 if 嵌套 场景 条件是层次的
