import os
from pathlib import Path


print(f'{"*" * 9} 当前执行文件 {"*" * 9}')
print(type(__file__))
print(__file__)


print(f'{"*" * 9} 当前目录 {"*" * 9}')
base_path = os.path.dirname(os.path.abspath(__file__))
print(type(base_path))
print(base_path)

print(os.getcwd())

print(Path.cwd())


print(f'{"*" * 9} 当前用户目录 {"*" * 9}')
print(os.path.expanduser("~"))
print(Path.home())


print(f'{"*" * 9} 路径拼接 {"*" * 9}')
print(os.path.join(base_path, "logs", "log.txt"))
print(Path(Path.cwd(), "logs", "log.txt"))

