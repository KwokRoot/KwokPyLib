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
print(type(d_str))
print(d_str)


print(f'{"*" * 9} dict 序列化与反序列化(json) {"*" * 9}')


# dict 序列化为 json字符串
print(f'{"*" * 3} 序列化 {"*" * 3}')

d_json_str = json.dumps(d, indent=4, ensure_ascii=False)
print(type(d_json_str))
print(d_json_str)

# json字符串 反序列化为 dict
print(f'{"*" * 3} 反序列化 {"*" * 3}')

print(type(json.loads(d_json_str)))
print(json.loads(d_json_str))


print(f'{"*" * 9} 对象 序列化与反序列化(json) {"*" * 9}')


class Cls(object):
    cls_attr1 = "cls_attr1"

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Cls):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


# json.dumps(cls, default=complex_encoder), 优先级高于 `cls=`
def complex_encoder(obj):
    if isinstance(obj, Cls):
        return obj.__dict__
    return json.dumps(obj);


# 对象 序列化为 json字符串
print(f'{"*" * 3} 序列化 {"*" * 3}')

cls = Cls("o1", "o2")
j_cls = json.dumps(cls, cls=ComplexEncoder)
print(type(j_cls))
print(j_cls)


class ComplexDecoder(json.JSONDecoder):
    def decode(self, obj):
        if isinstance(obj, str):
            return Cls(**json.loads(obj))
        return obj


# json字符串 反序列化为 对象
print(f'{"*" * 3} 反序列化 {"*" * 3}')

obj2 = json.loads(j_cls, cls=ComplexDecoder)
print(type(obj2))
print(obj2.__dict__)

