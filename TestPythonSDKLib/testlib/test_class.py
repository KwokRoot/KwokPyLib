# 创建类
class User(object):

    # 类属性(公有)
    x = "ok"
    # 类属性(私有)
    __y = "!"

    def __init__(self, id):
        self.id = id
        self.name = "default"
        self.__age = 18

    def getUserData(self):
        return f'id: {self.id}, name: {self.name}, {User.x}'

    # `@property` 装饰器来创建只读属性，将方法转换为相同名称的只读属性，可以实现在读取类属性前对数据进行预处理。
    @property
    def age(self):
        return self.__age + 1

    # `@*.setter` 装饰器必须在 `@property` 装饰器的后面，且两个被修饰的函数的名称必须保持一致，* 即为函数名称。
    @age.setter
    def age(self, value):
        self.__age = value + 1

    @age.deleter
    def age(self):
        print("@*.deleter")
        self.__age = 0

    # 静态方法，用 `@staticmethod` 进行修饰
    @staticmethod
    def getStaticMethod():
        return User.x + User.__y

    # 类方法，用 `@classmethod` 进行修饰，需要一个参数是类本身，通常将其命名为 cls。
    @classmethod
    def getClassMethod(cls):
        return cls.x + cls.__y


user1 = User(1)

print(f'{"*" * 9} 类属性 {"*" * 9}')

# 类属性 通过类名、实例都能调用
print(User.x)
print(user1.x)


print(f'{"*" * 9} 私有属性 {"*" * 9}')

# 私有属性 不能直接访问
# print(user1.__age)
# 私有属性 解释器会改名
print(user1._User__age)
print(user1.__dir__())
print(user1.__dict__)

# 私有类属性 不能直接访问
# print(User.__y)
# 私有类属性 解释器会改名
print(User._User__y)
print(User.__dict__)


print(f'{"*" * 9} 实例、类、静态方法 {"*" * 9}')

# 实例方法，能通过实例调用，不能通过类直接调用。
# print(User.getUserData())
print(user1.getUserData())

# 类方法 可通过 类、实例都能调用
print(User.getClassMethod())
print(user1.getClassMethod())

# 静态方法 可通过 类、实例都能调用
print(User.getStaticMethod())
print(user1.getStaticMethod())


print(f'{"*" * 9} `@property` 装饰器 {"*" * 9}')

print(user1._User__age)
print(user1.age)

user1.age=30
print(user1._User__age)
print(user1.age)

user1._User__age = 100
print(user1._User__age)
print(user1.age)

# 触发 `@age.deleter`
del user1.age
print(user1.age)

