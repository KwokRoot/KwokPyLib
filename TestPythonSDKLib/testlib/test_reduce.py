from functools import reduce

# 从 1 加到 100
print(reduce(lambda x, y: x + y, range(1, 101)))

# 阶层
print(reduce(lambda x, y: x * y, [i for i in range(1, 10)]))

