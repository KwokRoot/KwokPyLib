
with open("log.txt", "r", encoding="utf-8") as f1:
    for line in f1.readlines():
        print(line, end="")
    print(f1.fileno())

with open("log.txt", "r", encoding="utf-8") as f2:
    print(f2.read())
    print(f2.fileno())


print("*" * 36)


# 上例 f1、f2 文件打开编号和上次一样，可说明 with 可自动关闭 文件。
f3 = open("log.txt", "r", encoding="utf-8")
f4 = open("log.txt", "r", encoding="utf-8")
print(f3.fileno())
print(f4.fileno())


