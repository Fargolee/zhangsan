'''
print('hello world')  # 字符串
print(233)  # 整数
print(2.333)  # 小数
print(True)  # 布尔值
print(())  # 元组
print([])  # 数组
print({})  # 字典

print('哈哈', 22)
print('hh' + 'aa')
print('哈哈' * 10)
print(10 / 3 % 2)

'''
# a = float(input('请输入：'))
# b = float(input('请输入：'))
# print('input获取的内容：', a * b)

# a = input('请输入：')
# b = input('请输入：')
# c = float(len(a))
# d = float(len(b))
# print('和：', c+d)

# a = int(len(input('请输入：')))
# b = int(len(input('请输入：')))
# print('和：', a + b)

# a = float(input('请输入：'))
# b = float(input('请输入：'))
# print('和：', len(a + b))

# a = len(input('请输入：'))
# b = len(input('请输入：'))
# print('和：', a + b)


# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# 元组  下标，从0开始
# a = (1, 2, 3, 4,  '哈哈', '嘻嘻', True, False)

# 切片
# print(a[:4])
# print(a[-6:])

'''
a = [1, 2, 3, 4, '哈哈', '嘻嘻', True, False]
# a.append(5)
# a.insert(0, 0)
print(a)
a.pop(4)
print(a.pop(4))
# print(a.clear())
c = [0, 1, 2]
a.extend(c)
a.remove(4)
print(a)

'''
# print(a[-1], a[1])
# print(int(a[0]+1))
# print(a[4]*10)
# print(a.index(4))

# print(a[a.index(4)])
# print(a.index(4))
# print(a.count(4))

# b = (a, '哈哈', '嘻嘻')
# c = ('哈哈', b, '嘻嘻')
# # print(len(b))
# print(c[1][0][-3])

'''
字典的特点：
1、字典中的值没有顺序
2、字典中的类型必须是 键值对的结构 key:value
3、字典的值 是通过key去取这个value
'''
a = {'name': '张三', 0: '哈哈', 'age': 25}
# 取值
print(a['name'])
print(a[0])
# 新增
a['heigh'] = '183cm'
a['length'] = '18'
print(a)
# 修改
a['name'] = '李四'
print(a[0])

b = a.get('name')  # 获取
print(b)

a.update(name=111)  # 更新
print(a)

print(a.get('name'))
print(a['name'])

# print(a.get('name1'))  # 空值
# print(a['name1'])  # 报错


# del a["name"]
# print(a)
# del a[0]
# print(a)
