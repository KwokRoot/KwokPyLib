import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8]
np.array(data)

print(f'计数: {np.count_nonzero(data)}')
print(f'求和: {np.sum(data)}')
print(f'最大值: {np.max(data)}')
print(f'最小值: {np.min(data)}')
print(f'均值: {np.mean(data)}')
# np.average() 可计算加权平均
print(f'均值: {np.average(data)}')
print(f'方差: {np.var(data, ddof=1)}')
print(f'标准差: {np.std(data, ddof=1)}')

print(f'中位数: {np.median(data)}')
print(f'百分位: {np.percentile(data, [50, 99])}')

