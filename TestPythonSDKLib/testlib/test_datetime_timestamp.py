from datetime import datetime, date, timedelta
import time


# datetime  <->  [ 时间戳 / 时间结构体 ]  <->  time


# datetime 转 时间结构体
print(datetime.now().timetuple())

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


# 今日 0时 时间戳
print(int(time.mktime(date.today().timetuple())))

# time 获取某日 0 时 秒时间戳
print(time.mktime(time.strptime("2022-9-10 0:0:0", '%Y-%m-%d %H:%M:%S')))

# datetime 获取某日 0 时 秒时间戳
print(datetime.strptime("2022-9-10 0:0:0", '%Y-%m-%d %H:%M:%S').timestamp())

# 获取某时间间隔的 0时 秒时间戳
now = datetime.now()
print(int((now - timedelta(days=30, hours=now.hour, minutes=now.minute, seconds=now.second,
                           microseconds=now.microsecond)).timestamp()))


