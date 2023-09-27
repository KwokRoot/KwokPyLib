import os
import sys


print(f'{"="*18} 当前文件 {"="*18}')

# 当前文件
print(__file__)
# 被调用的脚本文件名或全路径，与操作系统有关
print(sys.argv[0])


print(f'{"="*18} 当前目录 {"="*18}')

# 当前目录
print(os.getcwd())
print(os.path.dirname(__file__))
print(os.path.abspath("."))
print(sys.path[0])


print(f'{"="*18} 拼接目录 {"="*18}')

# 基于 base 目录拼接目标目录
base_path = os.path.join(os.path.dirname(__file__), 'logs')
print(base_path)

base_path = os.path.abspath(os.path.join(__file__, os.pardir, 'logs'))
print(base_path)


print(f'{"="*18} pathlib 模块 {"="*18}')

# Python 3.4+ 引入了 pathlib 模块
from pathlib import Path

current_dir = Path(__file__).resolve().parent
print(current_dir)
print(current_dir.joinpath("logs", "info"))

