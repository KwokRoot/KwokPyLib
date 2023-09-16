from collections import ChainMap

d = {
    "1": "1",
    "3": "2",
    "5": "3",
    "2": "33",
    "4": "333",
    "6": "6"
}

print(f'{"*" * 9} dict 遍历 {"*" * 9}')


# 注 python3.6 +，dict 类型变为有序对象集合。
for k, v in d.items():
    print(f"{k} : {v}")

print(d.keys())
print(d.values())


print(f'{"*" * 9} dict 取值 {"*" * 9}')

try:
    d["666"]
except Exception as e:
    print("===有异常===")

# key 不存在 返回 None, 可设置默认值
print(d.get("666", "666"))


print(f'{"*" * 9} dict 排序 {"*" * 9}')

print(type(d.items()))
print(d.items())

# 默认根据 dict 类型 key 排序，即 元组 中的第一个元素排序。
print(sorted(d.items()))

# ！！！注：sorted() 返回类型为 list[tuple(Key, Value)] 类型列表，可通过 dict()、或者 字典推导式转换为 dict 类型。
print(type(sorted(d.items())))
print(dict(sorted(d.items())))
print({it[0]: it[1] for it in sorted(d.items())})

# 设置根据 元组 中的第 1 个元素排序，即 dict 的 key。
print(sorted(d.items(), key=lambda it: it[0]))

# 设置根据 元组 中的第 2 个元素倒序排序，即 dict 的 value。
print(sorted(d.items(), key=lambda it: it[1], reverse=True))

# 排序 dict，利用 字典推导式 实现 K、V 互换。
d_o = {it[1]: it[0] for it in sorted(d.items(), key=lambda it: it[0])}
print(d_o)


print(f'{"*" * 9} dict 合并 {"*" * 9}')


d1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

d2 = {
    "x": 7,
    "y": 8,
    "z": 9,
    "d": 10
}

print(f'{"*" * 3} ① ChainMap 合并 {"*" * 3}')

cm1 = ChainMap(d1, d2)
cm2 = ChainMap(d2, d1)
print(cm1.get("d"))
print(cm2.get("d"))
print(dict(cm1))

print(f'{"*" * 3} ② 解包 合并 {"*" * 3}')

d3 = {**d1, **d2}
print(d3)

print(f'{"*" * 3} ③ update 合并 {"*" * 3}')

print(d1.update(d2))
# 结果：None
print(d1)


print(f'{"*" * 9} 创建默认值 dict {"*" * 9}')

print(dict.fromkeys("ijk", 5))


