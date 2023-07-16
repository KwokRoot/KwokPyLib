import os

print(f'{"*" * 9} 获取当前路径 {"*" * 9}')

current_dir = os.getcwd();
print(current_dir)

base_path = os.path.dirname(os.path.abspath(__file__))
print(base_path)


print(f'{"*" * 9} 创建、移动(重命名)、删除文件夹 {"*" * 9}')

try:
    os.makedirs("/opt/1/11/111", exist_ok=True)

    # os.rename("/opt/1/11", "/opt/2")
    # 删除多层空目录，会递归删除上层空目录
    # os.removedirs("/opt/2/222")
    # 删除空目录，不会删除上层的空目录
    # os.rmdir("/opt/2/111", )
except OSError as e:
    print("抛 OSError 异常：", e)
    pass


print(f'{"*" * 9} 修改 cmd 编码 {"*" * 9}')
# 将 cmd 显示的字符编码从默认的 GBK 改为 UTF-8
os.system('chcp 65001')
res = os.system("dir")
os.system("python -V")
print(res)


print(f'{"*" * 9} 创建日志目录示例 {"*" * 9}')

# base_path = os.getcwd()
base_path = os.path.dirname(os.path.abspath(__file__))
# print(base_path)
my_path = os.path.join(base_path, "logs")
if not os.path.exists(my_path):
    os.makedirs(my_path, exist_ok=True)
my_log_path = os.path.join(my_path, "log.txt")
with open(my_log_path, "w+", encoding="utf-8") as f:
    pass


print(f'{"*" * 9} 获取文件描述符 {"*" * 9}')

# 获取文件描述符(文件标识)，经测试，Windows、linux 同一逻辑磁盘下，重命名、移动都不会发生改变，可用于日志采集。
# Python 在 Windows 系统、Linux 系统该方式均适用。
file_info = os.stat(my_log_path)
print(file_info)


print(f'{"*" * 9} 遍历文件目录 {"*" * 9}')

# 遍历文件目录
for root, dirs, files in os.walk("/opt/", topdown=True):
    for name in files:
        print(os.path.join(root, name))


print(f'{"*" * 9} 执行 shell 命令 {"*" * 9}')

# 执行 shell 命令
os.system("dir")
print("*" * 36)
# 解决中文文件名乱码
print(os.popen("dir").read())

