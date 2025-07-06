import statistics


data = [1, 2, 3, 4, 5, 6, 7, 8]

print(f'计数: {len(data)}')
print(f'求和: {sum(data)}')
print(f'最大值: {max(data)}')
print(f'最小值: {min(data)}')
print(f'均值: {statistics.mean(data)}')
print(f'方差: {statistics.variance(data)}')
print(f'标准差: {statistics.stdev(data)}')

print(f'中位数: {statistics.median(data)}')

# ## Python V3.8+
# print(f'百分位: {statistics.quantiles(data, n=100)[50]}')

