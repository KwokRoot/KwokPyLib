import pickle

print(f'{"*" * 9} dict 序列化与反序列化(pickle) {"*" * 9}')


# dict 序列化为 字节数组
d = {'1': 'a', '2': 'b'}
p = pickle.dumps(d)
print(type(p))
print(p)

# 字节数组 反序列化为 dict
d2 = pickle.loads(p)
print(type(d2))
print(d2)


print(f'{"*" * 9} 对象 序列化与反序列化(pickle) {"*" * 9}')


class Obj(object):
    cls_attr1 = "cls_attr1"

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


# 对象 序列化为 字节数组
obj = Obj("o1", "o2")
p_obj = pickle.dumps(obj)
print(type(p_obj))
print(p_obj)

# 字节数组 反序列化为 对象
obj2 = pickle.loads(p_obj)
print(type(obj2))
print(obj2)
print(obj2.__dict__)

