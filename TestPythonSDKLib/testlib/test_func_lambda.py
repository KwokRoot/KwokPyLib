from functools import reduce


def add1(arg1, arg2):
    return arg1 + arg2


add2 = lambda arg1, arg2: arg1 + arg2

print(add1(10, 20))
print(add2(10, 20))


print("*" * 36)


s = [1, 2, 3]

# filter()
print(list(filter(lambda x: x % 2 == 0, s)))

# map()
print(list(map(lambda x: x * x + 1, s)))

# reduce()
print(reduce(add1, s))
print(reduce(add2, s))

