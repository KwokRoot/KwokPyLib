from datetime import datetime, timedelta, date, time as datetime_time


# 时间戳  <->  datetime  <->  时间字符串


print("{0} 1-1 {0}".format("*" * 9))

# datetime 转 时间戳
ts_s = datetime.now().timestamp()
print(ts_s)

# 时间戳 转 datetime
datetime.fromtimestamp(ts_s)


print("{0} 1-2 {0}".format("*" * 9))

# datetime 转 时间字符串
time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(time_str)

# 时间字符串 转为 datetime
print(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f'))


print("{0} 1-3 {0}".format("*" * 9))


# 时间戳 [转 datetime] 转 时间字符串
print(datetime.fromtimestamp(ts_s).strftime("%Y-%m-%d %H:%M:%S.%f"))

# 时间字符串 [转 datetime] 转 时间戳
print(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f').timestamp())


print("*" * 36)


# 构造 datetime.date
print(date(2020, 10, 1))

# 构造 datetime.time
print(datetime_time(20, 10))

# 构造 datetime.datetime
datetime.combine(date(2020, 10, 1), datetime_time(20, 10))
print(datetime(2022, 10, 1))
print(datetime(2022, 10, 1, 9))


print("*" * 36)

# 时间戳是指格林威治时间 1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数。
print(datetime(1970, 1, 1).isoformat())
print(datetime(1970, 1, 2, 8, 0, 0).timestamp())
print(24 * 60 * 60)


print("*" * 36)


# 修改 datetime 某字段
print(datetime(2022, 10, 1, 9).replace(year=2050, hour=10))


print("*" * 36)


print(datetime.today().isoformat())
print(datetime.utcnow().isoformat())
# datetime.now(tz) 时区参数可选
print(datetime.now().isoformat())


print("*" * 36)


# datetime 转 时间结构体
print(datetime.now().timetuple())


