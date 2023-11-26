import math
import numpy as np

# ## 方差、标准差

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

avg_val = np.mean(a)
sum_val = [math.pow(i - avg_val, 2) for i in a]
print(sum_val)

# 总体方差
print(sum(sum_val) / len(a))
print(np.var(a))
# 样本方差
print(sum(sum_val) / (len(a) - 1))
print(np.var(a, ddof=1))

# 总体标准差
print(pow(sum(sum_val) / len(a), 1 / 2))
print(np.std(a))
# 样本标准差
print(pow(sum(sum_val) / (len(a) - 1), 1 / 2))
print(np.std(a, ddof=1))

