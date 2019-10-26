# 文件写入
"""
  7- 文件写模式：
        1- fo = open(fileDir,'w')
        2- 如果该路径下的文件存在---会清空！
        3- 如果该路径下的文件不存在---会新建！
        4- 在pycharm里面，你执行了fo.write('123')--可以直接写进去
        5- fo.write('123')--返回值---写的字符长度
        6- fo.flush() 强行写入文件
        7- fo.close() 关闭文件会强行写入文件
    8- 追加模式 a
        1- 只是为了在文件末尾追加内容而打开文件
    9- With open 方式
        1- with open(fileDir) as rFile:----rF = open(fileDir)
        2- 可以省略fo.close()
        3- 操作多个文件

"""
filefi = 'd:1.txt'
fo = open(filefi, 'w')  # 只写操作打开： 文件不存在--新建 存在会清空
fo.write('12356\nabcdhs')  # 原理是写入到缓存里--本质不会写入到文件离去
fo.flush()
fo.close()
# 文件的扩展用法
with open(filefi, "r") as efile, open('必填参数--路径', 'w')as wfile:
    # 不需要用close（） 操作多个文件
    efile.read()
    wfile.write('233q')
