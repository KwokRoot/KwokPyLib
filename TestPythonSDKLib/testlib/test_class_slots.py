class Student(object):

    # `__slots__` 目的是限制当前类所能拥有的属性，避免因为外部属性的操作导致类属性越来越难以管理。
    # __slots__ = ('name', 'sex', 'score')

    def __init__(self, name, sex, score):
        self.name = name
        self.sex = sex
        self.score = score


student = Student('Bob', 'Man', 100)
# 默认情况(无 `__slots__`)，实例可以动态地添加属性。
student.age = 12

print(student.__dict__)


