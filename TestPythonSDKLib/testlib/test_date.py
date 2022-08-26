import datetime
import time

print("*" * 36)


# time

# 获取默认格式时间戳
print(time.time())

# 获取毫秒时间戳
ts_ms = int(time.time() * 1000)
print(ts_ms)

# 秒时间戳转时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts_ms / 1000)))

# time 转 字符串，获取当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))

print("*" * 18)

# 时间字符串解析为时间元组
timeArray = time.strptime("202208231415", "%Y%m%d%H%M")
print(timeArray)

# 将时间元组转换为时间戳
ts_s = int(time.mktime(timeArray))
print(ts_s)

# 今日零点时间戳
print(time.mktime(datetime.date.today().timetuple()))

# 格式化时间戳为时间元组
timeArray = time.localtime(ts_s)

# 将时间元组转换为时间字符串
timeStr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(timeStr)


# 程序暂停秒
time.sleep(0.1)


print("*" * 36)


# datetime

# datetime 转 字符串，获取当前时间
time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(time_str)

# 字符串 转为 datetime
t = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f').timestamp()
print(t)

# 毫秒时间戳转时间字符串
print(datetime.datetime.fromtimestamp(ts_ms / 1000))


# 时间计算，保留到毫秒
print((datetime.datetime.now() - datetime.timedelta(days=1, hours=2)).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

# datetime 与 time 转化
print(type(datetime.datetime.now().fromtimestamp(time.time())))
print(type(time.localtime(time.mktime(datetime.datetime.now().timetuple()))))

