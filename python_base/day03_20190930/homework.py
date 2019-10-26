import re

# 用户控制台输入一串数字
# 判断用输入字符串的长度
# 判断用输入字符串是否全是数字
# 判断用户手机号是那个营业亭的
yidong = ['131', '132', '133']
liantong = ['134', '135', '136']
diajxin = ['138', '139']
moblie = input("请输入您的手机号码：")
if re.findall('^[0-9]+$', moblie):
    if len(moblie) == 11:
        i = moblie[:3]
        if i in yidong:
            print("该号码为中国移动")
        elif i in liantong:
            print("该号码为中国联通")
        elif i in diajxin:
            print("该号码为中国电信")
        else:
            print("该号码为其他号码")
    else:
        print("手机尾数不对")
else:
    print("手机号有非法字符")
