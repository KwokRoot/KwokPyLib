class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(self.name, '说话')

    def __repr__(self):
        return f'{{"name": "{self.name}", "age": "{self.age}"}}'


class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sex = '男'


class Police(Man, Person):
    def __init__(self, name, age):
        super().__init__(name, age)


police = Police("小王", "18")
print(police.sex)

