import functools

var = '1001'
print(int(var, base=2))

# 基于一个函数和该函数的参数来定义另外函数
int2 = functools.partial(int, base=2)
print(int2(var))
