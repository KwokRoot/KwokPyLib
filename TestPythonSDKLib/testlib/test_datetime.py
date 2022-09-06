from datetime import datetime, timedelta


# 时间戳  <->  datetime  <->  时间字符串


# datetime 转 时间戳
ts_s = datetime.now().timestamp()
print(ts_s)

# 时间戳 转 datetime
datetime.fromtimestamp(ts_s)


print("*" * 18)


# datetime 转 时间字符串
time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(time_str)

# 时间字符串 转为 datetime
print(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f'))


print("*" * 18)


# 时间戳 [转 datetime] 转 时间字符串
print(datetime.fromtimestamp(ts_s).strftime("%Y-%m-%d %H:%M:%S.%f"))

# 时间字符串 [转 datetime] 转 时间戳
print(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f').timestamp())


print("*" * 36)


# 时间计算，保留到毫秒
print((datetime.now() - timedelta(days=1, hours=2)).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


print("*" * 36)


# datetime 转 时间结构体
print(datetime.now().timetuple())


