from urllib import request
import json

url = r"http://es.com/_search"
data = {
    "size": 1,
    "sort": {"l_time": "desc"}
}

data = json.dumps(data)
# raw = bytes(data, "utf8")
raw = data.encode("utf-8")
headers = {'Content-Type': 'application/json'}

req = request.Request(url=url, headers=headers, data=raw)  # 构造请求
resp = request.urlopen(req, timeout=3).read().decode()  # 获取响应

print(json.loads(resp))
print(json.dumps(json.loads(resp), indent=4))

