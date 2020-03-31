
import requests
from dbtools import Db

db = Db("192.144.148.91", "ljtest", "123456", "ljtestdb")

url = "http://192.144.148.91:2333/get_title_img"
# headers = {'Content-Type': "application/json"}
# res = requests.get(url=url,headers=headers)
# print(res.text)
res = requests.get(url)
# print(res.json())
# print('\n')
data = res.json().get('data')
num = len(data)
res = db.chaxun("select count(*) from t_title_img where status = 0;")[0][0]

# res = db.chaxun("select count(*) from t_title_img where status = 0;")
# print(res[0][0])

if num == res:
    print('测试通过！')
else:
    print('测试失败！')