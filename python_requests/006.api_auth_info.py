import json

import requests

url = 'http://127.0.0.1:8080/api/auth/info'
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjIsImV4cCI6MTU4NDg4NjE3OCwiaWF0IjoxNTg0MjgxMzc4LCJpc3MiOiJvY2VhbmxlYXJuLnRlY2giLCJzdWIiOiJ1c2VyIHRva2VuIn0.s3HRmLveArnhXXb-3fpP37LbVx89DquT-Ws1K_Qw0L0"
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
"""
{
    "code": 200,
    "data": {
        "user": {
            "ID": 2,
            "CreatedAt": "2020-03-15T13:53:36Z",
            "UpdatedAt": "2020-03-15T13:53:36Z",
            "DeletedAt": null,
            "Name": "OUTdlkrYrl",
            "Telephone": "12345678901",
            "Password": "$2a$10$4xB58OSa7nyIxiNorJa0ruj2WM3AupL7uxUD9faR9i/.2mo6Ys/WO"
        }
    }
}
"""
