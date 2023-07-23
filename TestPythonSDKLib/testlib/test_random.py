import random


# 随机生成 [0,1) 范围内浮点数
print(random.random())


# 生成范围内整数
print(random.randint(3, 10))


# 生成范围内整数，可定义步长
print(random.randrange(10, 20, 2))


# 序列中随机选择一个
ls = ['Python', 'C', 'C++', 'C#', 'Java', 'Go', 'JavaScript', 'Nodejs', 'PHP']
print(random.choice(ls))
print(random.choice("HelloWorld"))

