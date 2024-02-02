import time
from datetime import datetime, timedelta, timezone, date as datetime_date, time as datetime_time, tzinfo

print(f'{"*" * 18} 时间戳  <->  datetime  <->  时间字符串 {"*" * 18}')

print(f'{"*" * 9} datetime 转 时间戳 {"*" * 9}')
ts_s = datetime.now().timestamp()
print(ts_s)

print(f'{"*" * 9} 时间戳 转 datetime {"*" * 9}')
dt = datetime.fromtimestamp(ts_s)
print(dt)


print(f'{"*" * 9} datetime 转 时间字符串 {"*" * 9}')
time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(time_str)

print(f'{"*" * 9} 时间字符串 转 datetime {"*" * 9}')
print(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f'))


print(f'{"*" * 9} 时间戳 [转 datetime] 转 时间字符串 {"*" * 9}')
print(datetime.fromtimestamp(ts_s).strftime("%Y-%m-%d %H:%M:%S.%f"))

print(f'{"*" * 9} 时间字符串 [转 datetime] 转 时间戳 {"*" * 9}')
print(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f').timestamp())


print("*" * 36)

print(f'{"*" * 9} 构造 datetime.date {"*" * 9}')
print(datetime_date(2020, 10, 1))

print(f'{"*" * 9} 构造 datetime.time {"*" * 9}')
print(datetime_time(20, 10))

print(f'{"*" * 9} 构造 datetime.datetime {"*" * 9}')
print(datetime.combine(datetime_date(2020, 10, 1), datetime_time(20, 10)))
print(datetime(2022, 10, 1))
print(datetime(2022, 10, 1, 9))


print("*" * 36)

# 时间戳是指格林威治时间 1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数。
print(datetime(1970, 1, 1).isoformat())
print(datetime(1970, 1, 2, 8, 0, 0).timestamp())
print(24 * 60 * 60)

print(datetime.today().isoformat("T"))
print(datetime.now().isoformat())
print(datetime.now(tz=timezone(timedelta(hours=0))))
print(datetime.utcnow().isoformat())

print(f'{"*" * 9} 时间戳 与 时区 {"*" * 9}')
dt = datetime(2024, 2, 1, 20, 30, 00, tzinfo=timezone(timedelta(hours=0)))
ts = dt.timestamp()

# 默认本地时区
dt2 = datetime.fromtimestamp(ts)
print(dt2)

dt3 = datetime.fromtimestamp(ts, tz=timezone(timedelta(hours=0)))
print(dt3)


print("*" * 36)

print(f'{"*" * 9} 修改 datetime 某字段 {"*" * 9}')
print(datetime(2022, 10, 1, 9).replace(year=2050, hour=10))


print("*" * 36)

print(f'{"*" * 9} datetime 转 时间结构体 {"*" * 9}')
print(datetime.now().timetuple())
print(time.mktime(datetime.now().timetuple()))

