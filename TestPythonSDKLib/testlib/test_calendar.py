import calendar

# 获取月份的天数
print(calendar.monthrange(2020, 2)[1])

# 获取给定日期的最后一天
date_str = "202101"
last_day_str  = str(calendar.monthrange(int(date_str[:4]), int(date_str[4:6]))[1])
print(last_day_str)
if len(date_str) < 8:
    date_str += last_day_str
print(date_str)

