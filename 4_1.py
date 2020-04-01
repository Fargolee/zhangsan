import requests
from dbtools import Db

db = Db("192.144.148.91", "ljtest", "123456", "ljtestdb")

# url = "http://192.144.148.91:2333/login"
# data = {"username": "lisi111","password": "a1234567"}
# res = requests.post(url=url,json=data)
# token = res.json()['data']['token']
# with open('token.txt','w') as f:
#     f.write(token)


with open('token.txt','r') as f:
    token = f.readline()

#用户发表灵感
url = "http://192.144.148.91:2333/inspirer/new"
data ={
"content":"淡黄的长裙，蓬松的头发"
}
headers = {'token':token}
res = requests.post(url=url,headers=headers,json=data)
# print(res.text)
a = res.json()['data']['inspirerid']
# print(a)

#获取灵感详情
url = "http://192.144.148.91:2333/get/inspirer"
headers = {'Content-Type': "application/json"}
params = {'iid':a}
res1 =requests.get(url=url,headers=headers,params=params)
# print(res1.text)

#用户修改灵感
url = "http://192.144.148.91:2333/inspirer/update"
data = {
"content":"Jony J:我太难了", 
"iid":a
}
headers = {'token':token}
res2 = requests.post(url=url,headers=headers,json=data)
# print(res2.text)

#用户删除灵感
url = "http://192.144.148.91:2333/inspirer/delete"
data = {
"iid":a
}
headers = {'token':token}
res3 = requests.post(url=url,headers=headers,json=data)
print(res3.text)