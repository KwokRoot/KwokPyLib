ls = [2, 4, 6, 8, 10]

print(f'{"*" * 9} 遍历 list {"*" * 9}')

for l in ls:
    print(f"{l}")


for i, l in enumerate(ls):
    print("%s -> %s" % (i, l))


print(f'{"*" * 9} 集合推导式 {"*" * 9}')

print([x for x in ls if x % 4 == 0])

print(list(x - 1 for x in ls))


print(f'{"*" * 9} 合并 list {"*" * 9}')

list1 = [1, 2, 3]
list2 = [6, 7, 8]

# 产生新的对象
list3 = list1 + list2
print(list3)

# 不产生新的对象
before_id = id(list1)
print(list1.extend(list2))
# 结果：None
print(list1)
print(id(list1) == before_id)


