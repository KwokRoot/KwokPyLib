a = (1, 2, 3)
b = [4, 5, 6]
c = [7, 8, 9, 0]


# 将可迭代对象打包成元组
ziped = zip(a, b, c)
print(list(ziped))


# 将元组解压为对象元组
ziped = zip(a, b, c)
a2, b2, c2 = zip(* ziped)
print(a2)
print(b2)
print(c2)


