class Person(object):
    def __init__(self, name, age):
        print("Person Class init")
        self.name = name
        self.age = age

    def speak(self):
        print(self.name, '我是人')

    def __repr__(self):
        return f'{{"name": "{self.name}", "age": "{self.age}"}}'


class Man(Person):
    def __init__(self, name, age):
        print("Man Class init")
        super().__init__(name, age)
        self.sex = '男'

    def speak(self):
        print(self.name, '我是男人')


class Police(Man, Person):
    def __init__(self, name, age):
        print("Police Class init")
        super().__init__(name, age)


police = Police("小王", "18")
print(police.sex)
police.speak()

# 查看多继承的调用顺序
print(Police.__mro__)


# `isinstance()` 第一个参数是实例，判断是否为该类或子类的实例。
print(isinstance(police, (Exception, Man, )))
# `issubclass()` 第一个参数是类名，判断是否为该类的子类。
print(issubclass(Police, (Exception, Man, )))

# 类的所有直接父类
print(Police.__bases__)
# 类的所有直接子类
print(Person.__subclasses__())


