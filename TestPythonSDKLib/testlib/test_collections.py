import collections


# 词频统计
l = ["a", 1, "b", 2, 'c', "c", 'd', 3, 3, 2, 3]
c = collections.Counter(l)
print(c.most_common(6))

for i in zip(c.keys(), c.values()):
    print(f"Word: {i[0]}, Count: {i[1]}")

