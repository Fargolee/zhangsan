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
for r in range(1, 31):
    print('红灯', str(r) + 's', end='  ')
print()
for g in range(1, 36):
    print('绿灯', str(g)+'s', end='  ')
print()
for y in range(1, 4):
    print('黄灯', str(y)+'s', end='  ')
print()

# 练习2
userinfo = {}
username = input('请输入账号：')
password = input('请输入密码：')
