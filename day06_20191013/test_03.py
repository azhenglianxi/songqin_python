# 循环嵌套：

# 嵌套循环执行顺序：
# 先从外层循环里面取出一个元素，再执行内层的循环
# 当内层的循环都执行完后，再继续执行外层循环
boy = ['1', '2', '3']
girs = ['yi', 'er', 'san']
for i in girs:
    for j in boy:
        print(i, j)
# 列表生成式
beforetax = [100000, 50000, 8000]
afterax = [int(one * 0.9) for one in beforetax if one > 5000]  # 比较简单的操作
print(afterax)

# 排序算法
alist = [6, 8, 0, 2, 5]  # ----升序
alist.sort()
print(alist)
print(alist[::-1])  # 1.切片  ：：-1 倒序
alist.reverse()  # 2.方法排序
print(alist)

# 冒泡排序的方法 要领：找n-1较大值 每次一次较大值是通过相邻元素比较，大的往后移
# 1.找n-1次最大值：
for i in range(0, len(alist) - 1):
    # 2.每一次较大值的获取：比较相邻的元素大小
    for j in range(0, len(alist) - i - 1):
        pass

"""
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
"""
