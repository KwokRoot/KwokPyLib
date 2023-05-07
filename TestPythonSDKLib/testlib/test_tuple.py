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


