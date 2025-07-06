# toolz 函数式编程 和 数据流操作
# pip install toolz
from toolz import count, pipe, compose

data = [1, 2, 3, 4, 5, 6, 7, 8]
print(count(data))


def increment(x):
    return x + 1


def double(x):
    return x * 2


# 使用 pipe 进行管道化数据处理，从左到右
r3 = pipe(3, increment, double)
print(r3)
# 等价于
print(double(increment(3)))


# 使用 compose 进行数据处理，从右到左
r4 = compose(increment, double)(3)
print(r4)
# 等价于
print(increment(double(3)))
