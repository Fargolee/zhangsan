import time
import pymysql

# for i in range(10):
#     time.sleep(1)
#     print(i)


# db = pymysql.connect(host='127.0.0.1', user='root',
#                      password='123456', db='liyuhe')
# cur = db.cursor()
# cur.execute("select * from t_class;")
# res = cur.fetchall()
# print(res)


"""
class 声明类的名字
类的名字首字母必须大写
面对对象编程
"""


class Girlfriend():
    def __init__(self):
        self.sex = '女'
        self.high = '170cm'
        self.weight = '55kg'
        self.hair = '大波浪'
        self.age = '18岁'

    def caiyi(self, num):
        if num == 1:
            print('胸口碎大石！')
        elif num == 2:
            print('唱跳rap')
        else:
            print('单手开瓶盖')

    def chuyi(self):
        print('啥都会')

    def work(self):
        print('开挖掘机')


class Nvpengy(Girlfriend):
    def work(self):
        print('修电脑')


# 类的实例化
zhang = Nvpengy()
zhang.caiyi(1)
zhang.work()
print(zhang.sex)

