# print('Hello World!')

# 判断
# a = 1
# b = 2
# if a > b:
#     print('a比b大')
# else:
#     print('b更大')


# age = int(input('请输入你的年龄：'))
# if age > 60:
#     print('好好活')
# elif age > 30:
#     print('好好干')
# elif age > 20:
#     print('好好浪')
# else:
#     print('好好玩')

# a = input('请输入：')
# if a in '0123456789':
#     a = int(a)
# else:
#     print('请输入正确的年龄：')
#     exit()
# if a > 20:
#     print('青年')
# else:
#     print('小伙')


# a = input('请输入：')
# if type(a) is int:
#     print(a+'是数字')
# elif type(a) is str:
#     print(a+'是字符串')
# else:
#     print('其他')


# a = 1
# while a < 10:
#     print(a)
#     a = a + 1

# jg = {}
# bjg = {}
# a = input('张三的成绩：')
# if a > 60:
#     jg.update(a)
# cj = {}

# cj_up = {}
# cj_low = {}
# student_list = ['张三', '李四', '王五', '浪晋', '流云', '希希', '小小', '陈二狗', '陈平安', '亚索']
# a = 0
# while a < len(student_list):
#     cj = int(input('请输入' + student_list[a] + '的成绩：'))
#     if cj >= 60:
#         cj_up[student_list[a]] = cj
#     else:
#         cj_low[student_list[a]] = cj
#     a = a + 1
# print(cj_up)
# print(cj_low)

# a = ['张三', '李四', '王五', '浪晋', '流云', '希希', '小小', '陈二狗', '陈平安', '亚索']
# for i in a:
#     print(i)

# b = list(range(0, 100, 2))
# print(b)


# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(i, 'x', j, '=', i * j, end='  ')
#     print()

"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
"""


"""
练习：
现在有10个学生的成绩，需要录入到系统中。
这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠、亚索
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
'''
highchengji = {}  # 定义了一个空字典，用来存储大于60的信息
lowchengji = {}  # 定义了一个空字典，用来存储小于60的信息
studentlist = ["张三", "李四", "王麻子", "浪晋", "流云",
    "希希", "小梁", "二狗", "陈平安", "朱珠", "亚索"]
a = 0  # 定义了一个变量，用来控制数组的下标的变化
while a < len(studentlist):  # 因为所有的人的信息的录入，都是要用input，所有写了循环，len判断了数组的长度，总长度-1就是最大的下标
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))  # 录入信息，为了方便判断，所以转换了格式
    if chengji >= 60:  # 判断分数
        highchengji[studentlist[a]] = chengji  # 存到字典中
    else:
        lowchengji[studentlist[a]] = chengji
    a = a + 1  # 控制下标变化，每一次循环，都+1
print("大于60的：", highchengji)
print("小于60的：", lowchengji)


'''
# 循环 continue break

# for i in range(10):
#     if i == 3:
#         continue #跳过
#     print(i)

# for i in range(10):
#     if i == 3:
#         break  # 中断
#     print(i)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if i == 3:
#             break  # 跳出这一层循环
#         print(i, 'x', j, '=', i * j, end='  ')
#     print()


# 方法
# def 方法的声明
# checkname 方法的名字
# username 方法的参数
# ''' 方法的说明 '''
# 方法的逻辑代码

# def checkname(username):


# def jia(a, b):
#     '''此方法的作用是实现两个数字相加 '''
#     if type(a) is int and type(b) is int:
#         print(a + b)
#     else:
#         print('输入的数据类型不正确')


# jia(1, 36)

def jia(a, b):
    '''此方法的作用是实现两个数字相加 '''
    if type(a) is int and type(b) is int:
        return a + b
    else:
        return '输入的数据类型不正确'


# print(jia(1, 36))

# 异常捕获
# try:
#     print(a + 1)
# except:
#     print('错误')

# 异常类
try:
    print(a + 1)
except Exception as c:
    print('错误', c)
