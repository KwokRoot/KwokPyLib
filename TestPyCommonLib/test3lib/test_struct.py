import struct

# # `struct` 模块是 Python bytes 对象与 C 结构体之间转换的类库。


# `@`: 本地; `=`: 本地; `<`: little-endian; `>`: big-endian; `!`: network(= big-endian);
print(struct.pack("@i", 0x01020304))
print(struct.pack("=i", 0x01020304))
print(struct.pack("<i", 0x01020304))
print(struct.pack(">i", 0x01020304))
print(struct.pack("!i", 0x01020304))


print("*" * 36)

# native byteorder(little-endian)
buffer = struct.pack("ihb", 1, 2, 3)
print(buffer)

print(struct.unpack("ihb", buffer))


# network byteorder(big-endian)
data = [1, 2, 3]
buffer = struct.pack("!ihb", *data)
print(buffer)
print(struct.unpack("!ihb", buffer))

# `i`: int(4个字节); `h`: short(2个字节); b: signed char(1个字节);
print(struct.calcsize("ihb"))
print(struct.calcsize("!ihb"))

