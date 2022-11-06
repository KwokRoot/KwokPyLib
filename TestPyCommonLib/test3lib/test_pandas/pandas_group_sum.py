import re

import pandas as pd
from matplotlib import pyplot as plt

lines = []
with open(r"pandas_group_sum.txt") as f:
    lines = f.read().splitlines()
print(len(lines))


p = re.compile(r'(?P<key>\S*)\s*(?P<val>\S*)')

kvs = []
for line in lines:
    m = p.match(line)
    if m:
        # print(line)
        kvs.append((m.group("key"), int(m.group("val"))))


df = pd.DataFrame(kvs, columns=["key", "val"])
# print(df.dtypes)

# 注：先创建空的`DataFrame`，再追加数据，该方式已过时。
# df = pd.DataFrame(columns=["key", "val"])
# for kv in kvs:
#     df = df.append({"key":kv[0], "val": int(float(kv[1]))}, ignore_index=True)


# 设置 `pandas` 打印展示效果
# 显示最大列数，None 为全部
pd.set_option('display.max_columns', None)
# 显示最大行数，None 为全部
pd.set_option('display.max_rows', None)
# 显示每列字段最大宽度
pd.set_option('max_colwidth', None)
# 显示行宽度
pd.set_option('display.width', None)

# 分组求和
df = df.groupby(["key"], as_index=True).sum().sort_values("val", ascending=False)

# 结果打印
print(df)

# 结果输出到 excel
# df.to_excel("结果.xlsx")

# 结果绘图
# 设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 坐标轴负号显示不正常及不能正常显示中文
plt.rcParams['axes.unicode_minus'] = False
# 默认为折线图
df.plot(kind='bar', title="统计图", figsize=(12, 8), legend=True, fontsize=18)

plt.show()

