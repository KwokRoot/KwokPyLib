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

    # 静态方法，用 @staticmethod 进行修饰
    @staticmethod
    def getStaticMethod():
        return User.x + User.__y


user1 = User(1)

# 类属性 通过类名、实例调用
print(User.x)
print(user1.x)

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

print(user1.getUserData())

# 静态方法 通过 类名、实例调用
print(User.getStaticMethod())
print(user1.getStaticMethod())


