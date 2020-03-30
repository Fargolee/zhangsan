# def checkname(username, password):
#     '''
#     自动判断
#     '''
#     # username = input('请输入账号：')
#     # password = input('请输入密码：')
#     if len(username) >= 5 and len(username) <= 8:
#         if username[0] in 'qazxswedcvfrtgbnhyujmiklop':
#             if len(password) >= 8 and len(password) <= 16:
#                 return True
#             else:
#                 return '密码不符合规范'
#         else:
#             return '账号的首字母必须小写'
#     else:
#         return '账号的长度不符合规范，请输入5-8位的账号'


# # checkname(username, password)
# print(checkname('Ahangsan', 'a12345678'))

'''
class GirlFriend():
    def __init__(self):  # 初始化，默认值
        self.sex = '女'
        self.high = '175cm'
        self.weight = '55kg'
        self.hair = '大波浪'
        self.age = '18岁'

    def caiyi(self, num):
        print('你性别为'+self.sex+'身高'+self.high+'体重' +
              self.weight+'发型'+self.hair+'年龄'+self.age+'女朋友开始了才艺表演')
        if num == 1:
            print('胸口碎大石')
        elif num == 2:
            print('唱跳rap')
        else:
            print('单手举高高')

    def work(self):
        print('开挖掘机！')

# 类的实例化
zhangsan = GirlFriend()

print(zhangsan.sex)
zhangsan.caiyi(2)
zhangsan.work()

'''


class GirlFriend():
    def __init__(self, sex, high, weigh, hair, age):  # 初始化，默认值
        self.sex = sex
        self.high = high
        self.weight = weigh
        self.hair = high
        self.age = age

    def caiyi(self, num):
        print('你性别为'+self.sex+'身高'+self.high+'体重' +
              self.weight+'发型'+self.hair+'年龄'+self.age+'女朋友开始了才艺表演')
        if num == 1:
            print('胸口碎大石')
        elif num == 2:
            print('唱跳rap')
        else:
            print('单手举高高')

    def work(self):
        print('开挖掘机！')


# 类的实例化
# zhangsan = GirlFriend('男', '180cm', '80kg', '锡纸烫', '28岁')

# print(zhangsan.sex)
# zhangsan.caiyi(2)
# zhangsan.work()

class Car():
    def __init__(self, pingpai, yanse, neishi, jilun):
        self.pingpai = pingpai
        self.yanse = yanse
        self.neishi = neishi
        self.jilun = jilun

    def bianxing(self):
        print('车子变身为大黄蜂')

    def fly(self):
        print('飞飞飞飞飞')


# zhangsan = Car('奥拓', '五颜六色', '豪华', '独轮车')
# zhangsan.bianxing()
# zhangsan.fly()


# 类的继承
# GirlFriend: 父类
# Nvpengy：子类
# object： 祖宗类

object： 祖宗类


class Nvpengy(GirlFriend):
    def work(self):  # 类的重写
        print('修电脑')


zhangsan = Nvpengy('女', '175', '110', '短发', '25')
zhangsan.work()
