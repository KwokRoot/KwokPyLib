# pip install python-dateutil
from dateutil.relativedelta import relativedelta

from datetime import datetime
from datetime import timedelta


print(f'{"*" * 18} dateutil.relativedelta {"*" * 18}')

# dateutil.relativedelta 支持月份加减，datetime.timedelta 不支持月份加减
for i in range(1, 12):
    time_delta = relativedelta(months=-i)
    date_str = (datetime.now() + time_delta).strftime("%Y%m")
    print(date_str)

    time_delta2 = timedelta(days=-i * 30)
    date_str2 = (datetime.now() + time_delta2).strftime("%Y%m")
    print(date_str2)

    print("*" * 6)


print(f'{"-" * 6} 计算日期之间的差值 {"-" * 6}')

# 2003-02-28
print(datetime(2003, 1, 31) + relativedelta(months=+1))

dt1 = datetime(2018, 12, 11, 12, 0, 0)
dt2 = datetime(2024, 1, 27, 17, 30, 0)

delta = relativedelta(dt2, dt1)
print(f"{delta.years}年 {delta.days}天 {delta.hours}时 {delta.minutes}分")


print(f'{"*" * 18} dateutil.parser {"*" * 18}')

from dateutil import parser
#
parser_datetime = parser.parse('2018/12/16')
print(type(parser_datetime))
print(parser_datetime)

print(parser.isoparse("2018-12-16T12:00:00+08:00"))


print(f'{"*" * 18} dateutil.rrule {"*" * 18}')

# 每月第一个周一的日期序列
from dateutil import rrule

rule = rrule.rrule(rrule.MONTHLY, byweekday=rrule.MO(1), dtstart=dt1, until=dt2)

for dt in rule:
    print(dt)

print(f'{"-" * 6}{"-" * 6}')

# 间隔 3年 时间序列
dl = list(rrule.rrule(rrule.YEARLY, interval=3, count=6, dtstart=datetime(2018, 12, 11)))
print(dl)

