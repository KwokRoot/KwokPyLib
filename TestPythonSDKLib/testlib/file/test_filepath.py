import os

# 当前文件
print(type(__file__))
print(__file__)


# 当前文件夹
base_path = os.path.dirname(os.path.abspath(__file__))
print(type(base_path))
print(base_path)
print(os.path.join(base_path, "logs", "log.txt"))


# 当前文件夹
current_dir = os.getcwd()
print(type(current_dir))
print(current_dir)
