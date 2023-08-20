class Class:
    def __init__(self, students):
        self.students = students

    # 定义 `__len__` 内置方法，可使用 `len(对象)` 调用
    def __len__(self):
        return len(self.students)

    # 定义 `__add__` 内置方法，对象可使用算术运算符 `+`，进行调用
    def __add__(self, other):
        return self.students + other.students


students = ['LiMing', 'Danny', 'Jenny']
class_ = Class(students)
print(len(class_))


other_students = ['李明', '韩梅梅', '李雷']
class2_ = Class(other_students)
print(class_ + class2_)

