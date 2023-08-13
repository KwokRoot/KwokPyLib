# class 对象 与 dict对象相互转化
print(f'{"*" * 9} 示例1 {"*" * 9}')


class A(object):
    cls_attr1 = "c_a1"

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


a = A("a1", "a2")

# class 对象 转 dict对象，注：不能输出类变量
print(type(a.__dict__))
print(a.__dict__)

# dict对象 转 class 对象
print(type(A(**a.__dict__)))
print(A(**a.__dict__).__dict__)


print(f'{"*" * 9} 示例2 {"*" * 9}')


class B(object):
    cls_attr1 = "c_b1"

    def __init__(self, attr1, attr2, **keys):
        self.attr1 = attr1
        self.attr2 = attr2
        self.__dict__.update(keys)

    # dict(对象)时, 调用类中的 keys() 方法，程序将依照字典取值的方式尝试获得这些键对应的值。
    def keys(self):
        return ('attr1', 'cls_attr1', 'attr2')

    # 当使用字典取值时: 比如 b['attr1'], 将会调用类中的 __getitem__() 方法
    def __getitem__(self, item):
        return getattr(self, item)


b = B("b1", "b2")

# class 对象 转 dict对象
print(type(dict(b)))
print(dict(b))

# dict对象 转 class 对象
print(type(B(**dict(b))))
print(B(**dict(b)).__dict__)


print(f'{"*" * 9} 示例3 {"*" * 9}')


class C(object):
    cls_attr1 = "c_c1"

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def to_dict(self):
        return {
            "cls_attr1": self.cls_attr1,
            "attr1": self.attr1,
            "attr2": self.attr2,
        }

    @classmethod
    def from_dict(cls, d: dict):
        c = cls(d.get("attr1"), d.get("attr2"))
        if d.get("cls_attr1"): c.cls_attr1 = d.get("cls_attr1")
        return c


c = C("c1", None)

# class 对象 转 dict对象
print(type(c.to_dict()))
print(c.to_dict())

# dict对象 转 class 对象
print(type(C.from_dict(c.to_dict())))
print(C.from_dict(c.to_dict()).__dict__)

