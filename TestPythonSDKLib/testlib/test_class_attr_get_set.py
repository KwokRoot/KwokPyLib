class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getData(self):
        return f'name: {self.name}, age: {self.age}'

    # 类中同时重写了 `__str__` 和 `__repr__`，当调用 `print(实例对象)` 时，Python 优先调用 `实例对象.__str__()`，
    # 当在交互式界面直接敲实例对象时，Python 调用 `实例对象.__repr__()`。
    # def __str__(self):
    #     return 'this is class __str__'

    def __repr__(self):
        return 'this is class __repr__'

    # 实例化对象 变为 可调用对象
    def __call__(self, a):
        print('call func be invoked')
        print(a)


print(f'{"*" * 3} 示例1-1 {"*" * 3}')

p = Person("Kwok", 18)
print(p)
print(p.name)
try:
    print(p.a)
except AttributeError as e:
    print("AttributeError: ", e)


print(f'{"*" * 3} 示例1-2 {"*" * 3}')
print(p.__dict__)
p.b = 'b 值'
print(vars(p))
print(p.b)

# setattr(object, name, value)
setattr(p, 'c', 'c 值')

# getattr(object, name[, default])，注：重新了 `__getattr__`，hasattr、getattr 默认行为受影响
print(hasattr(p, 'd'))
print(getattr(p, 'd', 'd值'))


print(f'{"*" * 3} 示例1-3 {"*" * 3}')

# `对象名()` 等价 调用`__call__()`方法
p('Me1')
p.__call__("Me2")

# 方法也是可调用对象，有 `__call__` 方法
print(p.getData.__call__())


print(f'{"*" * 3} 示例1-4 {"*" * 3}')
# `hasattr()` 函数返回实例否包含指定名称的属性或者方法，但该函数有一个缺陷，即它无法判断指定的名称，到底是类属性还是类方法。
# `__call__()` 弥补 `hasattr()` 函数的短板。

print(hasattr(p, "name"))
# True
print(hasattr(p.name, "__call__"))
# False

print(hasattr(p, "getData"))
# True
print(hasattr(p.getData, "__call__"))
# True
