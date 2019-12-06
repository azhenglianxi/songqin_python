# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/11/29

import pymysql

# 建立数据库连接
db = pymysql.connect("47.105.139.174", "root", "root_password","python_lianxi")

# 获取操作游标
cu = db.cursor()


# 构造sql语句
sql = """
insert into python_lianxi.sq_course(id, `name`, `desc`, display_idx)
values (5, 'golang', 'go语言学习', 5);
"""

# 执行SQL语句
cu.execute(sql)
# 提交到数据库
db.commit()


# # 获取返回值
# data = cu.fetchall()
#
#
# print(data)


# 释放资源
cu.close()
db.close()

# 一次性插入多条数据的两种sql写法
"""
insert into plesson.sq_course(id, `name`, `desc`, display_idx)
values (6, 'golang6', 'go语言学习', 6),
	(7, 'golang7', 'go语言学习', 7),
	(8, 'golang8', 'go语言学习', 8),
	(9, 'golang9', 'go语言学习', 9),
	(10, 'golang10', 'go语言学习', 10);

insert into plesson.sq_course(id, `name`, `desc`, display_idx)
select 11, 'golang6', 'go语言学习', 11 union
select 12, 'golang6', 'go语言学习', 12 union
select 13, 'golang6', 'go语言学习', 13 union
select 14, 'golang6', 'go语言学习', 14 union
select 15, 'golang6', 'go语言学习', 15 union
select 16, 'golang6', 'go语言学习', 16;
"""