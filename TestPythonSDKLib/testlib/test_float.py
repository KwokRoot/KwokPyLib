import math

# 科学计数法
f = "1.1852456e+03"
f = float(f)
print(f)


# 四舍五入
print(round(f))

# 四舍五入，保留 2位 小数
print(round(f, 2))

# 向下取整
print(math.floor(f))

# 向上取整
print(math.ceil(f))

