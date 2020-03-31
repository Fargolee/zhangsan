
import pymysql


class Db:
    """
    这个是用来操作数据库的类
    """

    def __init__(self, host, user, password, dbname, port='3306'):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.port = port

    def chaxun(self, sql):
        """
        这个方法是查询数据库的数据 DQL语句
        """
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, db=self.dbname)  # 连接数据库
        cursor = db.cursor()  # 获取游标
        try:
            cursor.execute(sql)  # 使用游标来执行sql语句
            res = cursor.fetchall()  # 获取所有结果
            # print(res)  # res 返回的属于二元数组
            db.close()
            return res
        except Exception as e:
            return 'sql语句错误!', e

    # a = input('请输入sql语句：')
    # b = chaxun(a)
    # for i in b:
    #     print(i)

    # sql = "select * from t_user limit 3;"
    # a = chaxun(sql)
    # # print(a)
    # for i in a:
    #     print(i[0], i[1])
    def xiugai(self, sql):
        """
        修改数据库里的数据 DML
        """
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, db=self.dbname)  # 连接数据库
        cursor = db.cursor()  # 获取游标
        try:
            cursor.execute(sql)  # 使用光标来执行sql语句
            db.commit()  # 提交、应用
            db.close()
            return True
        except Exception as e:
            return 'sql语句错误！', e

    def regist(self, username, password):
        username = input('请输入账号：')
        password = input('请输入密码：')
        if len(username) >= 5 and len(username) <= 8:
            if username[0] in 'qazxswedcvfrtgbnhyujmkiolp':
                # if username[0] == username[0].lower():
                if len(password) >= 8 and len(password) <= 16:
                    # return '注册成功'
                    return "insert into t_user (username,password) values ('{}','{}');".format(
                        username, password)
                else:
                    return '密码不符合规范'
            else:
                return '账号的首字母必须小写开头'
        else:
            return '账号不符合规范'
# sql = "select * from t_user"
# a = xiugai(sql)
# print(a)
