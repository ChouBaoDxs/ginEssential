import json

import requests

url = 'http://127.0.0.1:8080/api/auth/login'
data = {
    'telephone': '12345678901',
    'password': '123456'
}

res = requests.post(url, data)
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
"""
{
    "code": 200,
    "data": {
        "token": "11"
    },
    "message": "注册成功"
}
"""