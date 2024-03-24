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
# 结果：True


print(f'{"*" * 9} 过滤 list {"*" * 9}')

ls2 = ["PYTHON", "JAVA", "C", "NODE.JS", "JAVASCRIPT", "HTML", "VB.NET"]

# ## 常规遍历过滤
ls2_1 = []
for l in ls2:
    if 'JAVA' in l:
        ls2_1.append(l)
print(ls2_1)

# ## 列表推导式 + if 过滤
ls2_2 = [l for l in ls2 if "JAVA" in l]
print(ls2_2)

# ## 使用 `filter()` 方法过滤
l2_3 = list(filter(lambda x: "JAVA" in x, ls2))
print(l2_3)


