from pathlib import Path

v_path = Path(r"F:\opt\test.txt")

# 读、写文本
v_path.write_text("hello 中国", encoding="utf-8")
print(v_path.read_text("utf-8"))

# 返回文件对象
if v_path.exists():
    with v_path.open("r", encoding="utf-8") as f:
        print(f.read())

# 读、写字节
v_path.write_bytes("hello 中国".encode("utf-8"))
print(v_path.read_bytes().decode("utf-8"))


