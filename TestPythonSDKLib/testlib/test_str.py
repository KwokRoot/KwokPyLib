s = b"13"
print(s)
print(s.decode())

print(str(s).isascii())
print(str(s).isalpha())
print(str(s).isnumeric())
print(str(s).isdigit())
print(str(s).isdecimal())

print("*" * 18)

print(s.decode().isascii())
print(s.decode().isalpha())
print(s.decode().isnumeric())
print(s.decode().isdigit())
print(s.decode().isdecimal())


print("*" * 36)

# str.format()
name = "kwok"
print(f"姓名：{name}")
print("姓名：{name}".format(name="k"))


print("*" * 36)

# 编码
print("Hello World . 你好".encode("unicode_escape"))
print((u'\uFFFD'.encode('utf-8') * 2).decode("gbk"))

print("中国.jpg".encode("utf-8").decode("ISO-8859-1"))


print("*" * 36)

str_list = ["I", "Love", "Python"]
print(" ".join(str_list))


print("*" * 36)

print(str.format("Hello {name}, you are {age} years old.", name="Alice", age=18))
print(str.format("Hello {}, you are {} years old.", "Alice", 18))
print(str.format("Hello {1}, you are {0} years old.", 18, "Alice"))

