import requests

payload = {'key1': 'value1', 'key2': ['value2', "123"]}

r = requests.get('https://httpbin.org/get?a1=1', params=payload)

print(r.json())

