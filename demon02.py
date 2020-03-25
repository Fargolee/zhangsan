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
