import numpy as np

# 创建填充 `1`(ones) 或 `0`(zeros) 的 n 维数组
d1 = np.ones((3, 2), dtype=np.int_)
print(d1)


# 创建给定列表数组
d2 = np.array([["aaa", "bbb", 1], ["x", "y", 2]], dtype=np.str_)
print(d2)


# 创建随机 n 维数组
d3 = np.random.randint(1, 10, (2, 3))
print(d3)

