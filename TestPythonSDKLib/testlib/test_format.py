import math

# 重复字符串的便捷方式 及 字符串格式化的便捷方式：
print("=" * 36)
print("总计: %s" % len(range(3)))
print("=" * 36)


# 拓展：
# 字符串格式化其他2种格式：

# # Python2.6+ 可使用 `str.format()`。format() 函数中大括号 `{}`、 `:` 作为特殊字符代替 `%`
print("总计: {}".format(len(range(6))))

# # f-string` - Python3.6+ 引入的字符串格式化。(推荐)
print(f"总计: {len(range(9))}")


print("=" * 36)


# str.format() 占位参数传入方式：
# 位置方式传入
print("my name is {1}, age is {0} .".format("Kwok", 28))

# 字典(dict)方式传入
print("my name is {name}, age is {age} .".format(name='Kwok', age=28))
print(str.format("my name is {name}, age is {age} .", name="Kwok", age=28))

d = {'name': 'Kwok', 'age': 28}
print("my name is {name}, age is {age} .".format(**d))

# 列表(list)方式传入
l = [28, "Kwok"]
print("my name is {1}, age is {0} .".format(*l))
# # 列表索引
print("my name is {0[0]}, age is {0[1]} .".format(l))


print("=" * 36)


# 填充与格式化
# # 左对齐
print('{0:*<10}'.format(bin(7)))
# # 右对齐
print('{0:*>10}'.format(bin(7)))
# # 居中对齐
print('{0:*^10}'.format(bin(7)[2:]))

# # 千分位格式化
print('{:,}'.format(1234678987654321))


print("=" * 36)


# 精度与进制
# # 精度
print('{0:.9f}'.format(math.pi))
# # 二进制
print('{0:b}'.format(10))
# # 八进制
print('{0:o}'.format(10))
# # 十六进制
print('{0:x}'.format(10))


