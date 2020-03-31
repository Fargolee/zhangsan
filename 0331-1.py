import requests
from dbtools import Db

db = Db("192.144.148.91", "ljtest", "123456", "ljtestdb")

url = "http://192.144.148.91:2333/login"
data = {
    "username": "lisi111",
    "password": "a1234567"
    }
res = requests.post(url=url,json=data)
token = res.json()['data']['token']
# print(token)
with open("token.text",'w') as f:
    f.write(token)

with open("token.text",'r') as f:
    token = f.readline()
url = "http://192.144.148.91:2333/inspirer/new"
data = {'content':"淡黄的长裙，蓬松的头发"}
headers = {'token':token}
res = requests.post(url=url,headers=headers,json=data)
print(res.text)