# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/11/29

import pymysql

# 建立数据库连接
db = pymysql.connect("47.105.139.174", "root", "root_password", "Test")

# 获取操作游标
cu = db.cursor()


# 构造sql语句
sql = """
select *
from plesson.sq_course
where `name` = 'python';
"""

# 执行SQL语句
cu.execute(sql)


# 获取返回值
data = cu.fetchall()


print(data)


# 释放资源
cu.close()
db.close()