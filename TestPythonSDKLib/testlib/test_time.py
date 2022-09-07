import time


# 时间戳  <->  时间结构体  <->  时间字符串


# 默认格式时间戳
print(time.time())

# 毫秒时间戳
ts_ms = int(time.time() * 1000)
print(ts_ms)

# 时间结构体
time_struct = time.localtime()
print(time_struct)

# 时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S"))


print("*" * 18)


# 时间结构体 转 秒时间戳
ts_s = int(time.mktime(time_struct))
print(ts_s)

# 秒时间戳 转 时间结构体
print(time.localtime(ts_s))


print("*" * 18)


# 时间字符串 转 时间结构体
print(time.strptime("202209062206", "%Y%m%d%H%M"))

# 时间结构体 转 时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time_struct))


print("*" * 18)


# 秒时间戳 [转 时间结构体] 转 时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts_s)))

# 时间字符串 [转 时间结构体] 转 秒时间戳
print(time.mktime(time.strptime("202208231415", "%Y%m%d%H%M")))


print("*" * 36)


# 程序暂停(秒)
time.sleep(0.1)


