from datetime import datetime, timedelta, timezone
import pytz

all_timezones = pytz.all_timezones
print(all_timezones)

print("*" * 36)

print(pytz.country_timezones('cn'))

print("*" * 36)

tz1 = pytz.timezone('Asia/Shanghai')
print(type(tz1))
print(tz1)
print(datetime.fromtimestamp(datetime.now().timestamp(), tz1))

print("*" * 18)

tz2 = timezone(timedelta(hours=+8))
print(type(tz2))
print(tz2)
print(datetime.fromtimestamp(datetime.now().timestamp(), tz2))

