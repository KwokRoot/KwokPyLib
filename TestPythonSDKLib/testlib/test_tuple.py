# 元组定义
tup = ('one', 1, "一")
print(type(tup))


# 元组解包
k, v, e = ('one', 1, "一")
print(k, v, e)


# 元组列表转换为字典(字典推导式)
tuple_list = [('one', 1), ('two', 2), ('three', 3)]

# ## 方式一
d = dict(tuple_list)
print(d)

# ## 方式二
d = {k: v for k, v in tuple_list}
print(d)

# ## 方式三 - 示例①
d = {tup[0]: tup[1] for tup in tuple_list}
print(d)

# ## 方式三 - 示例② 该方式对于大于 2个元素的元组，更灵活。
tuple_list = [(1, 'one', 'a'), (2, 'two', 'b'), (3, 'three', 'c')]
d = {tup[1]: tup[0] for tup in tuple_list}
print(d)


# ## 元组对应元素相加
print(f'{"*" * 3} 元组对应元素相加 {"*" * 3}')

t1 = (1, 2, 3)
t2 = (1, 2, 3)

# ！！！注，元组直接相加为元组元素合并，并非对应元素相加
print(t1 + t2)
# 输出: (1, 2, 3, 1, 2, 3)

# 方式一
t12 = (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])
print(t12)
# 输出: (2, 4, 6)

# 方式二
l2 = []
for i in range(min(len(t1), len(t2))):
    l2.append(t1[i] + t2[i])
print(tuple(l2))
# 输出: (2, 4, 6)

# 方式三
t3 = tuple(x + y for x, y in zip(t1, t2))
print(t3)
# 输出: (2, 4, 6)

# 方式四
t4 = tuple(sum(i) for i in zip(t1, t2))
print(t4)
# 输出: (2, 4, 6)

# 方式五
t5 = tuple(map(sum, zip(t1, t2)))
print(t5)
# 输出: (2, 4, 6)

# # 方式六：使用 numpy 第三方类库转化 元组 为 numpy数组，以矩阵形式相加
# np1 = np.array(t1)
# np2 = np.array(t2)
# t6 = tuple(np1 + np2)
# print(t6)
# # 输出: (2, 4, 6)


