newlist = []


def mySort(list):
    if (type(list).__name__ == 'list'):
        while len(list) > 0:
            temp = min(list)
            newlist.append(temp)
            list.remove(temp)
        print(newlist)

    else:
        print("参数必须是列表")


mySort([2, 9, 4, 6, 1])
