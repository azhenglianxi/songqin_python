# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/11/29

import MySQLdb

# 获取数据库连接
db = MySQLdb.connect(host="192.168.0.102", user="songqin", passwd="songqin", db="plesson",
                     port=3306, charset="utf8")

# 获取操作游标
cu = db.cursor()

# 构造SQL
sql = """
delete from plesson.sq_course
where id > 4;
"""
# 执行SQL
cu.execute(sql)
# 提交到数据库执行
db.commit()

# 释放资源
cu.close()
db.close()
