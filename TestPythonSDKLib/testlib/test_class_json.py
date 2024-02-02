import json


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print(f'{"*"*18} 对象 序列化 json字符串 {"*"*18}')

# 定义一个 MyClass 类的实例
obj = MyClass('Kwok', 18)

# 对象 转换成 字典
obj_dict = vars(obj)
# obj_dict = obj.__dict__
print(obj_dict)

# 字典 转换成 JSON字符串
obj_json = json.dumps(obj_dict)
print(obj_json)

# 合并步骤
print(json.dumps(MyClass('Kwok', 18).__dict__))


print(f'{"*"*18} json字符串 反序列化 对象 {"*"*18}')

# JSON字符串 转换成 字典
obj_dict2 = json.loads(obj_json)

# 字典 转换成 对象
obj2 = MyClass(**obj_dict2)

print(type(obj2))
print(obj2.name)

# 合并步骤
print(MyClass(**json.loads(obj_json)).age)

