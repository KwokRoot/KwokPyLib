import json

d = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "hi": "你好"
}

# 直接输出字典类型，注意单引号。
print(d)
d_str = str(d);
print(d_str)

# 对象序列化为 json
d_json_str = json.dumps(d, indent=4, ensure_ascii=False)
print(d_json_str)

# json 反序列化为对象
print(json.loads(d_json_str))
print(type(json.loads(d_json_str)))
