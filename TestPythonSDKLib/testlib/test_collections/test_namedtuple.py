from collections import namedtuple

# 创建一个 namedtuple 类
Person = namedtuple('Person', ['name', 'age', 'sex'])

# 使用 namedtuple 创建的类创建一个实例对象
p = Person('Kwok', 18, 'man')

# 使用 namedtuple 对象访问属性
print(p.name)
print(p.age)
print(p.sex)

print(p._asdict())


try:
    p.work = "devops"
except Exception as e:
    print(f'异常：{e}')


