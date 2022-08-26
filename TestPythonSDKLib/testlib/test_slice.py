obj = [0, 1, 2, 3, 4, 5, 6]
s = slice(1, 6, 2)
print(obj[s])
print(obj[1:6:2])

# obj[start : stop : step] 等价于 obj[slice(start, stop, step)]
