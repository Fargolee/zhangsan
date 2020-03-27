# date 0323
# a = int(len(input('请输入：')))
# b = int(len(input('请输入：')))
# print('和：', a + b)

# a = float(input('请输入：'))
# b = float(input('请输入：'))
# print('和：', len(a + b))

# a = len(input('请输入：'))
# b = len(input('请输入：'))
# print('和：', a + b)

# # date 0324
# name = input('用户名：')
# age = input('年龄：')
# sex = input('性别：')
# a = {}
# a.update(用户名=name, 年龄=age, 性别=sex)
# # a.update(年龄=age)
# # a.update(性别=sex)
# print(a)

# date 0325
"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
"""
# 练习1
# a = '红灯'
# for r in range(1, 31):
#     print('红灯', str(r) + 's', end='  ')
# print()
# for g in range(1, 36):
#     print('绿灯', str(g)+'s', end='  ')
# print()
# for y in range(1, 4):
#     print('黄灯', str(y)+'s', end='  ')
# print()

# light = {'红灯': 30, '绿灯': 35, '黄灯': 3}
# # while True: 死循环
# for i in light:
#     for j in range(light[i]):  # j （0-30）
#         print(i, '倒计时还有：', light[i]-j, '秒')  # light[i]-j 30-（0-30）倒计时

# 练习2
# userinfo = {}
# username = input('请输入账号：')
# password = input('请输入密码：')
# if 4 < len(username) < 9 and username.lower() == username:
#     if 5 < len(password) < 13 and password.lower() == password.lower():
#         userinfo[username.lower()] = password
#     else:
#         print('密码格式错误，请重新输入')
# else:
#     print('账号格式错误，请重新输入')
# print(userinfo)

# username = input('请输入账号：')
# password = input('请输入密码：')
# if len(username) >= 5 and len(username) <= 8:
#     if username[0] == username[0].lower():
#         if len(password) >= 8 and len(password) <= 12:
#             print('注册成功')
#         else:
#             print('6-12')
#         print('ok')
#     else:
#         print('首字母小写')
# else:
#     print('5-8位')
#


def regist():
    username = input('请输入账号：')
    password = input('请输入密码：')
    if len(username) >= 5 and len(username) <= 8:
        if username[0] is a['']:
            # if username[0] == username[0].lower():
            if len(password) >= 8 and len(password) <= 12:
                print('注册成功')
            else:
                print('6-12')
        else:
            print('首字母小写')
    else:
        print('5-8位')


regist()
