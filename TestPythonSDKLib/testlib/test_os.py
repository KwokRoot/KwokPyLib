import os

try:
    os.makedirs("/opt/1/11/111", exist_ok=True)
    os.rename("/opt/1/11", "/opt/2")
except OSError as e:
    print(e)
    pass


print("*" * 36)


# 将 cmd 显示的字符编码从默认的 GBK 改为 UTF-8
os.system('chcp 65001')
res = os.system("dir")
os.system("python -V")
print(res)


print("*" * 36)


# base_path = os.getcwd()
base_path = os.path.dirname(os.path.abspath(__file__))
print(base_path)

my_path = os.path.join(base_path, "logs")
if not os.path.exists(my_path):
    os.makedirs(my_path, exist_ok=True)

my_log_path = os.path.join(my_path, "log.txt")

with open(my_log_path, "w+", encoding="utf-8") as f:
    pass


print("*" * 36)


# 获取文件描述符(文件标识)，经测试，Windows、linux 同一逻辑磁盘下，重命名、移动都不会发生改变，可用于日志采集。
# Python 在 Windows 系统、Linux 系统该方式均适用。
file_info = os.stat(my_log_path)
print(file_info)


print("*" * 36)


# 遍历文件目录
for root, dirs, files in os.walk("/opt/", topdown=True):
    for name in files:
        print(os.path.join(root, name))

