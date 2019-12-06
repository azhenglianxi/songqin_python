# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/11/29

import pymysql

# 打开数据库连接
db = pymysql.connect("47.105.139.174", "root", "root_password", "Test")


# 获取操作游标
cu = db.cursor()


# 使用 execute 方法执行sql语句
cu.execute("SELECT VERSION()")

# 获取执行结果
data = cu.fetchone()  #

print("database version is:", data)


# 释放资源
cu.close()
db.close()
