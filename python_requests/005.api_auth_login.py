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
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjIsImV4cCI6MTU4NDg4NjE3OCwiaWF0IjoxNTg0MjgxMzc4LCJpc3MiOiJvY2VhbmxlYXJuLnRlY2giLCJzdWIiOiJ1c2VyIHRva2VuIn0.s3HRmLveArnhXXb-3fpP37LbVx89DquT-Ws1K_Qw0L0"
    },
    "message": "注册成功"
}
"""