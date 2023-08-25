# Python 自动打包和解包
fruits = ['apple', 'orange', 'banana']
fruit1, fruit2, fruit3 = fruits

print(fruit1)
print(fruit2)
print(fruit3)


print("*" * 36)


numbers = [1, 2, 3, 4, 5]
num1, _, *num3 = numbers
print(num1)
print(_)
print(num3)
print(*num3)


print("*" * 36)


# 解包交换变量的值
a = 10
b = 20
a, b = b, a
print(a, b)


print("*" * 36)


d = {'a': 1, 'b': 2}
print(*d.keys())
print(*d.values())
print(*d.items())
print(*d.popitem())
