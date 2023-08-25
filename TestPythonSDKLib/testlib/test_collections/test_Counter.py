from collections import Counter

# 词频统计
c = Counter('hello')
print(c.most_common())

c.update('world')
print(c.most_common())

c.subtract('world')
print(c.most_common())


# 删除计数值为 0 或 负数 的元素
c += Counter()
print(c.most_common())


# 词频 TOP-N
print(c.most_common(3))


print(c)
for i in zip(c.keys(), c.values()):
    print(f"Word: {i[0]}, Count: {i[1]}")

