import csv

# 读取 `csv` 文件
with open(r"D://opt/user.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


print("*" * 36)


with open(r"D://opt/user.csv", "r", encoding="utf-8") as f2:
    lines = f2.read().splitlines()
    for line in lines:
        print(line.split(","))

