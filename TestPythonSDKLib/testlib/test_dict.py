
d = {
    "1": "1",
    "3": "2",
    "5": "3",
    "2": "33",
    "4": "333",
    "6": "6"
}

# dict 遍历
for x, y in d.items():
    print(f"{x} : {y}")

print("*" * 36)


# dict 取值
try:
    d["666"]
except Exception as e:
    print("===有异常===")

# key 不存在 返回 None, 可设置默认值
print(d.get("666", "666"))


print("*" * 36)


# dict 排序

print(d.items())

# 默认根据 dict 类型 key 排序，即 元组 中的第一个元素排序。
print(sorted(d.items()))

# 设置根据 元组 中的第 1 个元素排序，即 dict 的 key。
print(sorted(d.items(), key=lambda s: s[0]))

# 设置根据 元组 中的第 2 个元素排序，即 dict 的 value。
print(sorted(d.items(), key=lambda s: s[1]))

# 利用 字典推导式 排序 dict，注 python3.6 +，dict 类型变为有序对象集合。
d_o = {i[0]: i[1] for i in sorted(d.items(), key=lambda s: s[0])}
print(d_o)

