from datetime import datetime, timedelta, date, time as datetime_time
import time


# datetime  <->  [ 时间戳 / 时间结构体 ]  <->  time


print("{0} 1-1 {0}".format("*" * 9))

# datetime 转 时间结构体
print(datetime.now().timetuple())


print("{0} 1-2 {0}".format("*" * 9))

# time [转 时间戳] 转 datetime
print(datetime.fromtimestamp(time.time()))

# datetime [转 时间戳] 转 时间结构体
print(time.localtime(datetime.now().timestamp()))

# datetime [转 时间结构体] [转 时间戳] 转 时间结构体
print(time.localtime(time.mktime(datetime.now().timetuple())))


print("*" * 36)


# time 获取 当前时间字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# datetime 获取 当前时间字符串
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


print("*" * 36)

print("{0} 2-1 {0}".format("*" * 9))

# time 获取某日 0 时 秒时间戳
print(time.mktime(time.strptime("2022-9-10 0:0:0", '%Y-%m-%d %H:%M:%S')))

# datetime 获取某日 0 时 秒时间戳
print(datetime.strptime("2022-9-10 0:0:0", '%Y-%m-%d %H:%M:%S').timestamp())


print("{0} 2-2 {0}".format("*" * 9))

# 获取某时间间隔的 0时 秒时间戳
now = datetime.now()
print((now - timedelta(days=30, hours=now.hour, minutes=now.minute, seconds=now.second,
                           microseconds=now.microsecond)).timestamp())


print("{0} 2-3 {0}".format("*" * 9))

# 当日 0时 秒时间戳
print(time.mktime(date.today().timetuple()))
print(datetime.combine(date.today(), datetime_time.min).timestamp())
print(datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).timestamp())

# 当日 23:59:59 秒时间戳
print(datetime.combine(date.today(), datetime_time.max).timestamp())
print(datetime.today().replace(hour=23, minute=59, second=59, microsecond=999999).timestamp())


print("*" * 36)


# 时间间隔 timedelta 对象，用于时间的计算。
print(datetime.now() + timedelta(days=0, hours=0, minutes=0, seconds=0,
                                 milliseconds=0, microseconds=0, weeks=1))

# 时间计算，保留到毫秒
print((datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

# datetime +-
timedelta_obj = datetime(2022, 10, 1, 9) - datetime(2022, 9, 10)
print(timedelta_obj.days)
print(timedelta_obj.total_seconds())


