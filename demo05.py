import requests

# url = "http://192.144.148.91:2333/login"

# payload = "{\r\n\"username\":\"lisi111\", \r\n\"password\":\"a1234567\" \r\n}\r\n"
# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "ddd25dc9-03ec-4734-be25-53acf981f043"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

#post型接口
url = "http://192.144.148.91:2333/login"
headers = {
    'Content-Type': "application/json"
    }
data = {
    "username": "lisi111",
    "password": "a1234567"
    }
res = requests.post(url=url, headers=headers, json=data)
# print(res.text) #text 以字符串/文本的格式显示
res1 = res.json() #josn 以字典格式显示
# print(type(res1))
print(res1)
# print(res1['data']['token'])
msg = res1.get('msg')
status = res1.get('status')
# if status == 200:
#     print('登录成功！测试通过！')
# else:
#     print('登录失败')
if msg == '登录成功！':
    print('登录成功！测试通过！')
else:
    print('登录失败')

#get型接口
# url = "http://192.144.148.91:2333/showversion"
# headers = {'Content-Type': "application/json"}
# res = requests.get(url=url,headers=headers)
# print(res.text)