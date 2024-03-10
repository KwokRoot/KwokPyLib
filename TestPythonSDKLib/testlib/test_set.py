# set 创建
s1 = {1, 2, 3}
print(type(s1))
# 输出：<class 'set'>

# `{}` 默认创建的是字典
s2 = {}
print(type(s2))
# 输出：<class 'dict'>

# 空 set 创建
s3 = set()
print(type(s3))
# 输出：<class 'set'>

print("*" * 36)

A = set([1, 2, 3, 6])
B = set([6, 7, 8, 9])

# 交集
print(A & B)
print(A.intersection(B))

print("*" * 36)

# 并集
print(A | B)
print(A.union(B))

print("*" * 36)

# 差集
print(A - B)
print(A.difference(B))

print("*" * 36)

# 对称差集(集合 A 和 B 中不属于 A&B 的元素)
print(A ^ B)
print(A.union(B).difference(A.intersection(B)))

print("*" * 36)

# 从集合中 删除 一个随机元素。
print(A.pop())

# 删除集合中的指定元素，如果该元素不存在，不会引发错误。
A.discard(0)

# 删除集合中的指定元素，如果该元素不存在，则引发错误。
try:
    A.remove(0)
except KeyError as e:
    print("*** 异常 ***")

# 两个集合 是否 不包含共同的元素(交集为 null)
print(A.isdisjoint(B))

# A集合 是否是 B 的子集
print(A.issubset(B))

# A集合 是否包含 B集合
print(A.issuperset(B))


