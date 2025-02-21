import string


# digits：包含所有数字字符
print(f'{"-" * 18} string.digits {"-" * 18}')
print(string.digits)

# ascii_letters：包含所有 ASCII 字母（小写和大写）
print(f'{"-" * 18} string.ascii_letters {"-" * 18}')
print(string.ascii_letters)

# ascii_lowercase：包含所有 ASCII 小写字母
print(f'{"-" * 18} string.ascii_lowercase {"-" * 18}')
print(string.ascii_lowercase)

# ascii_uppercase：包含所有 ASCII 大写字母
print(f'{"-" * 18} string.ascii_uppercase {"-" * 18}')
print(string.ascii_uppercase)

# hexdigits：包含十六进制数字字符（0-9, a-f, A-F）
print(f'{"-" * 18} string.hexdigits {"-" * 18}')
print(string.hexdigits)

# octdigits：包含八进制数字字符（0-7）
print(f'{"-" * 18} string.octdigits {"-" * 18}')
print(string.octdigits)

# punctuation：包含所有 ASCII 标点符号字符
print(f'{"-" * 18} string.punctuation {"-" * 18}')
print(string.punctuation)

# whitespace：包含所有 ASCII 空白字符（如空格、制表符、换行符等）
print(f'{"-" * 18} string.whitespace {"-" * 18}')
print(string.whitespace)

# printable：包含所有 ASCII 可打印字符（包括空白字符）
print(f'{"-" * 18} string.printable {"-" * 18}')
print(string.printable)


print("*" * 36)

# 创建一个 Template 对象
template = string.Template("Hello $name, you are $age years old.")
# 使用 substitute 方法进行字符串替换
result = template.substitute(name="Alice", age=18)
print(result)


print("*" * 36)

# 创建一个 Formatter 对象
formatter = string.Formatter()
# 格式化字符串
formatted_string = formatter.format("Hello {name}, you are {age} years old.", name="Alice", age=18)
print(formatted_string)


print("*" * 36)

# 将字符串中的每个单词的首字母大写
text = "hello world, this is python!"
capitalized_text = string.capwords(text)
print(capitalized_text)


