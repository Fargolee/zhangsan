# import dbtools  # 1
# from dbtools import chaxun  # 2
from dbtools import Db

# a = dbtools.chaxun("show tables;")  # 对应 1
# b = chaxun("show tables;")  # 对应 2
# print(a)
# print(c)

# db = Db("192.144.148.91", "ljtest", "123456", "ljtestdb")
# b = db.chaxun("show tables;")
# print(b)


# 格式化字符串
username = input('请输入账号：')
password = input('请输入密码：')
sql = "insert into t_user (username,password) values ('{}','{}');".format(
    username, password)
print(sql)
