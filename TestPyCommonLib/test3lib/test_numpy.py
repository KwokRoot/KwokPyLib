import numpy as np

# 创建填充 `1`(ones) 或 `0`(zeros) 的 n 维数组
d1 = np.ones((3, 2), dtype=np.int_)
print(d1)

print("*" * 36)

# 创建给定列表数组
d2 = np.array([["aaa", "bbb", 1], ["x", "y", 2]], dtype=np.str_)
print(d2)
# 数组的类型
print(d2.dtype)

print("*" * 36)

# 创建随机 n 维数组
d3 = np.random.randint(1, 10, (2, 3))
print(d3)
# 数组的纬度
print(d3.shape)
# 数组的转置
d3t = d3.T
print(d3t)
print(d3t.shape)

print("*" * 36)

# 数组数据导出、导入
# 从内存导出到文件
np.savez_compressed("/opt/data", d1=d1, d2=d2, d3=d3, d3t=d3t)
# 从文件导入内存
np_zf = np.load("/opt/data.npz")
# 获取某数组
print(np_zf["d1"])


