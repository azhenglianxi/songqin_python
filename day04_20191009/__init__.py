print(max(34, 57, 22, 11, 88))
print(max([34, 57, 22, 11, 88]))
print(max((34, 57, 22, 11, 88)))


def t2(para):
    para = 3


b = [1]
t2(b)
print(b)
print('my name is jack'.split(' ')[-1])


def getName(srcStr):
    return srcStr.split('the name is ')[1].split(',')[0]


print(getName('A pretty boy come in, the name is Patrick, level 194'))
print('A pretty boy come in, the name is Patrick, level 194'.split('the name is '))
print('A pretty boy come in, the name is Patrick, level 194'.split('the name is ')[1])
