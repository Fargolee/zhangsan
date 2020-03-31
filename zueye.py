

from dbtools import Db
def regist(self, username, password):
        username = input('请输入账号：')
        password = input('请输入密码：')
            if username[0] in 'qazxswedcvfrtgbnhyujmkiolp':
                # if username[0] == username[0].lower():
                if len(password) >= 8 and len(password) <= 16:
                    return True
                    # return "insert into t_user (username,password) values ('{}','{}');".format(
                    #     username, password)
                else:
                    return '密码不符合规范'
            else:
                return '账号的首字母必须小写开头'
        else:
            return '账号不符合规范'

db = Db("192.144.148.91", "ljtest", "123456", "ljtestdb")
username = input('账号：')
password = input('密码：')
res = regist(username,password)
if res == True:
    db.chaxun("select * from t_user where username = '{}';".format(username))
    if len(res) == 0:
        res = db.xiugai("insert into t_user (username,password) values ('{}','{}');".format(username,password))
        print('注册成功！',res)
    else:
        print('账号已存在！')
else:
    print(res)