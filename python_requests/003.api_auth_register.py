import json

import requests

url = 'http://127.0.0.1:8080/api/auth/register'
data = {
    'name': '',
    'telephone': '12345678901',
    'password': '123456'
}

res = requests.post(url, data)
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
