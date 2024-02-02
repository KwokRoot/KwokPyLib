# `f-string` Begin Python 3.6+
from datetime import datetime, timezone, timedelta

a = 10
print("a: %s" % a)
print("a: {}".format(a))
print(f"a: {a}")

print(f"a * a = {a * a}")

# Python 3.8+
# print(f"{a * a = }")
# 输出：a * a = 100


print(f'{"*"*18} 占位符转义 {"*"*18}')

# 在 `f-string` 中使用大括号 {} 来表示占位符时，如果要在字符串中嵌套大括号，应该使用双大括号 `{{}}` 来表示
type = "json"
print(f'{{ "type": "{type}", "a": {a} }}')

# 集合及字典输出，需要加`()`
name = "kwok"
print(f'{({name})}')
print(f'{({"name": name})}')

# `f-string`不能出现 '\'
x = "\\"
print(f'{x}')


print(f'{"*"*18} 整数进制转换 {"*"*18}')

print(f'{"*"*6} 2进制 {"*"*6}')
print(f'{a:b}')
print(f'{"*"*6} 8进制 {"*"*6}')
print(f'{a:o}')
print(f'{"*"*6} 10进制 {"*"*6}')
print(f'{a:d}')
print(f'{"*"*6} 16进制(小写) {"*"*6}')
print(f'{a:x}')
print(f'{"*"*6} 16进制(大写) {"*"*6}')
print(f'{a:X}')


print(f'{"*"*18} 进制带前缀输出 {"*"*18}')

print(f'{"*"*6} 2 进制 {"*"*6}')
print(bin(a))
print(f'{a:#b}')
print(f'{"*"*6} 8 进制 {"*"*6}')
print(oct(a))
print(f'{a:#o}')
print(f'{"*"*6} 10进制 {"*"*6}')
print(f'{a:#d}')
print(f'{"*"*6} 16进制(小写) {"*"*6}')
print(hex(a))
print(f'{a:#x}')
print(f'{"*"*6} 16进制(大写) {"*"*6}')
print(f'{a:#X}')


print(f'{"*"*18} 日期 {"*"*18}')

dt = datetime(2024, 2, 1, 20, 30, 00, tzinfo=timezone(timedelta(hours=8)))
print(f'{dt:%F}')
print(f'{dt:%X}')
print(f'{dt:%Y%m%d}')


print(f'{"*"*18} 其他 {"*"*18}')

print(f'{"*"*6} 数字分割 {"*"*6}')
b = 10000
print(f'{b:,d}')
print(f'{b:_b}')

print(f'{"*"*6} 数字正负 {"*"*6}')
# `+`：显示正负号；`-`：显示负号、不显示正号；
print(f'{123:+d} {-123:+d} {123:-d}')

print(f'{"*"*6} 小数保留 {"*"*6}')
# 默认保留 6 位小数
print(f'{a:f}')
print(f'{a:.2f}')
# 8个字符长度 + 保留2位小数
print(f'{a:08.2f}')

print(f'{"*"*6} 字符处理 {"*"*6}')
ascii = 97
print(chr(ascii))
print(f'{ascii:c}')

print(f'{"*"*6} 数字填充 {"*"*6}')
# 只能用 0 或者 空格来填充
print(f'{10:032b}')
print(f'{10:32b}')

print(f'{"*"*6} 字符填充 {"*"*6}')
# 右对齐
print(f'{name:>8}')
# 居中对齐
print(f'{name:^8}')
# 左对齐
print(f'{name:<8}')
# 填充字符（`*`） + 对齐
print(f'{name:*>8}')
print(f'{name:*^8}')
print(f'{name:*<8}')


print(f'{"*"*18} 实现 `__repr__` 打印 {"*"*18}')

birthday = "2024-02-01"
# `__str__()` 与 `__repr__()`
print("select name from where birthday > %s" % birthday)
print("select name from where birthday > %r" % birthday)
print(f"select name from where birthday > '{birthday}'")
print(f"select name from where birthday > {birthday!r}")
print(f"select name from where birthday > {birthday!a}")

