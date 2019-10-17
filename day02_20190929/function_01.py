# 封装删除列表中制定的全部数据
blist = [10, 10, 10, 10]


def counts(age, blist):
    while age in blist:
        blist.remove(age)
    print(blist)


counts(10, blist)
