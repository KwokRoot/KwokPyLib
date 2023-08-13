import sys

print(f'{"*" * 9} 获取当前 Python 环境路径 {"*" * 9}')
print(">>>" + str(sys.path))

# 添加 Python 环境路径
sys.path.append(__file__)
print(">>>" + str(sys.path))


print(f'{"*" * 9} 获取 Python 启动加载的模块 {"*" * 9}')
print(sys.modules)


print(f'{"*" * 9} 获取 Python 版本信息 {"*" * 9}')

# 获取 Python 版本
print(sys.version)
# 获取操作系统平台
print(sys.platform)

# 获取 Python 详细版本信息
print(sys.version_info)
print(f"{sys.version_info.major}.{sys.version_info.minor}")

this_python = sys.version_info[:2]
min_version = (3, 6)
if this_python < min_version:
    print("ERROR: " + " ".join("python 版本不符合要求."))
    sys.exit(-1)


print(f'{"*" * 9} 获取 Python 执行时输入的参数 {"*" * 9}')

# 获取 Python 执行时输入的参数
print(len(sys.argv))
print(sys.argv)
print(sys.argv[0])


print(f'{"*" * 9} 获取系统编码 {"*" * 9}')
print(sys.getdefaultencoding())


if __name__ == '__main__':
    pass

