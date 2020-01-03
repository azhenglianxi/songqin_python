# 定义数组
reslist = []
dict_log = {}
# 首先读取文件
file_log_path = 'log.txt'
# 读取文件
with open(file_log_path, 'r') as file_log:
    contents = file_log.read()
    filebuffer = contents.split('\n')
    del filebuffer[0], filebuffer[-1]
    # 遍历文件，
    resdict = {}
    for i in filebuffer:
        temp = i.split('\t')
        # print(temp)
        # 获取文件类型的集合(通过切片获取列表数据)
        file_type = temp[0].split('.')[-1].strip()
        # 获取文件大小的集合
        file_size = int(temp[1])
        # 归类统
        #         inFlag  =False
        #         # 5- 统计----同类型----最好--最快方法--用字典(键值)统计  {'类型1'：大小}---预习作业--4行代码
        #         # [['类型1'，大小1]，['类型2'，大小2]，['类型3'，大小3]]
        #         inFlag = False  # 初始值---标志法
        #         # 如果--有该行的类型：----直接累加列表里面的该类型大小
        #         # 匹配---for
        #         for one in reslist:  # one--每一个子列表  ['类型1'，大小1]---如果结果列表为空，他不会遍历
        #             if file_type == one[0]:   # one[0]代表一个子列表
        #                 print(one)
        #                 one[1] += file_size
        #                 inFlag = True  # 标记已经累加完成
        #                 # 当匹配完成；累加--不需要再遍历
        #                 break  # 结束循环
        #
        #         # 结果列表没有该行的类型：----新增这个组合列表
        #         if inFlag == False:
        #                 reslist.append([file_type,file_size])
        #     print(reslist)
        #
        if file_type not in resdict:
            resdict[file_type] = file_size
        else:
            resdict[file_type] += file_size

#         #判断字典是否存在key
#         if file_type in dict_log.keys():
#         #取出这个类型value 值
#             temp=dict_log.get(file_type)
#             dict_log[file_type]=temp
#         else:
#             dict_log[file_type] += file_size
print(resdict)
