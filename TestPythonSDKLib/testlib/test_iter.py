print(f'{"*" * 9} 可迭代对象 {"*" * 9}')
# 可迭代对象的 iter()、next() 方法
iter_obj = iter((1, 2, 3))
print(iter_obj.__next__())
print(type(iter_obj))
while True:
    try:
        print(next(iter_obj))
    except StopIteration as e:
        print("抛 `StopIteration` 异常")
        break


print(f'{"*" * 9} 生成可迭代对象<generator>的方法 {"*" * 9}')


# 方法 1
def make_iter():
    for i in range(3):
        yield i


iter_obj1 = make_iter()
print(type(iter_obj1))

for i in iter_obj1:
    print(i)

# 再次获取为空
print('-' * 6)

for i in iter_obj1:
    print(i)


# 方法 2
iter_obj2 = (i for i in range(6))
print(type(iter_obj2))

print(iter_obj2)
print(list(iter_obj2))

print(f'{"*" * 3} 示例对比 {"*" * 3}')

# 注列表推导式中的 `[]` 换成 `()` 就是生成器表达式。
list_obj = [i for i in range(6)]
print(type(list_obj))

