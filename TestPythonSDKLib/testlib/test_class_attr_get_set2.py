print(f'{"*" * 9} 示例1 {"*" * 9}')


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # `__getattr__` 函数：如果属性在实例字典(self.__dict__)以及对应的类中查找失败，那么会调用到类的 `__getattr__` 函数。
    # 即：object.__getattr__(self, name) 是一个对象方法，当找不到对象的属性时会调用这个方法。
    def __getattr__(self, key):
        print('__getattr__: %s' % key)
        return 'key: `{}` 不存在'.format(key)

    # `__setattr__` 函数：在属性赋值时被调用，并且将值存储到实例字典(self.__dict__)中。
    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print('__setattr__: %s' % self.__dict__)


print(f'{"*" * 3} 示例1-1 {"*" * 3}')

p = Person("Kwok", 18)
print(p)
# 注：实例中存在的属性，《不》调用 `__getattr__`
print(p.name)
# 注：实例中不存在的属性，调用 `__getattr__`
print(p.a)


print(f'{"*" * 3} 示例1-2 {"*" * 3}')
p.b = 'b 值'
print(p.b)

# getattr(object, name[, default])，注：重新了 `__getattr__`，hasattr、getattr 默认行为受影响
print(hasattr(p, 'd'))
print(getattr(p, 'd', 'd值'))


print(f'{"*" * 9} 示例2 {"*" * 9}')


class Test(object):
    def __init__(self, attr=''):
        self.__attr = attr

    def __call__(self, name):
        return name

    def __getattr__(self, key):
        if self.__attr:
            key = '{}.{}'.format(self.__attr, key)
        else:
            key = key
        print(key)
        return Test(key)


t = Test()
result = t.a.b.c('Kwok')
print(result)

