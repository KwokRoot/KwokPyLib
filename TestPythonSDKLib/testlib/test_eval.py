d = {
    "a": 1,
    "b": 2,
    "c": 3

}
print(d)


print("*" * 36)


# 字符串表达式计算
print(eval("2 * 3"))

# 字符串表达式使用上文变量参与计算
print(eval("d['a'] + d['b'] + d['c']"))
a = 1
b = 2
print(eval("a + b"))

print("*" * 36)

# 字符串数据源 转为 python 数据类型
print(eval("{'a': 1, 'b': 2, \"c\": 3}"))
print(type(eval("{'a': 1, 'b': 2, 'c': 3}")))

print(type(eval("{'111', '333', '222'}")))

print(type(eval("[('111', 1.0), ('222', 2.0), ('333', 3.0), ('000', 6.0)]")[0]))
