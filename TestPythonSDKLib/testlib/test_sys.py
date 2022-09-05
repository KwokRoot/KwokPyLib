import sys

print(">>>" + str(sys.path))


print("*" * 36)


# 获取 Python 执行时输入参数
print(len(sys.argv))
print(sys.argv)
print(sys.argv[0])


print("*" * 36)


# 获取 Python 版本信息
print(sys.version_info)
print(f"{sys.version_info.major}.{sys.version_info.minor}")

this_python = sys.version_info[:2]
min_version = (3, 6)
if this_python < min_version:
    print("ERROR: " + " ".join("python 版本不符合要求."))
    exit(1)


if __name__ == '__main__':
    pass

