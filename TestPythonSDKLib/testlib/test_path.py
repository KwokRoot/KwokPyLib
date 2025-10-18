from pathlib import Path

file_path = Path(r"F:\opt\test.json.txt")
if not file_path.exists():
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch(exist_ok=True)


print(f'{"*" * 9} 文件属性判断 {"*" * 9}')
print(file_path.exists())
print(file_path.is_file())
print(file_path.is_dir())
print(file_path.is_symlink())


print(f'{"*" * 9} 文件名及后缀 {"*" * 9}')
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.suffixes)


print(f'{"*" * 9} 文件路径 {"*" * 9}')
print(file_path.as_uri())
print(file_path.absolute())
print(Path("."))
print(Path(".").absolute())
# 路径分割
print(file_path.parts)
print(list(file_path.parents))
# 路径拼接
print(file_path.parent.joinpath("logs", "log.txt"))


print(f'{"*" * 9} 文件目录 {"*" * 9}')
# 根目录
print(file_path.anchor)
# 父目录
print(file_path.parent)
# 用户目录
print(Path.home())
# 当前目录
print(Path.cwd())


print(f'{"*" * 9} 文件/目录信息 {"*" * 9}')
print(file_path.lstat())
print(file_path.parent.lstat())


print(f'{"*" * 9} 目录遍历 {"*" * 9}')
print(list(file_path.parent.iterdir()))
print(file_path.match("*.txt"))
# 根据路径匹配规则,遍历当前目录
print(list(file_path.parent.glob("*.txt")))
# 根据路径匹配规则,递归遍历当前目录及子目录
print(list(file_path.parent.rglob("*.txt")))


print(f'{"*" * 9} 文件读写 {"*" * 9}')

# 文件读写文本(`w`覆盖模式)
file_path.write_text("hello 中国", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))

# 文件读写字节(`wb`覆盖模式)
file_path.write_bytes("hello 中国".encode("utf-8"))
print(file_path.read_bytes().decode("utf-8"))
