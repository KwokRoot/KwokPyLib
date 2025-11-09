import sys


print(f'{"*" * 9} 字符 与 int 相互转化 {"*" * 9}')

# 字符 转 int
char = 'a'
unicode_value = ord(char)
print(f"字符: '{char}' 对应的 Unicode 是: {unicode_value}")

# int 转 字符
unicode_value = 97
char = chr(unicode_value)
print(f"Unicode: {unicode_value} 对应的字符是: '{char}'")


# 其他方式(不推荐)

# 字符 转 int
char = 'a'
unicode_value = int.from_bytes(str.encode(char), byteorder=sys.byteorder)
print(unicode_value)

# int 转 字符
unicode_value = 97
char = int.to_bytes(unicode_value, 1, byteorder=sys.byteorder).decode()
print(char)

