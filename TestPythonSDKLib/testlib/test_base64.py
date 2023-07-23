import base64
from base64 import b64encode, b64decode

print(f'{"*" * 9} base64 加解密 {"*" * 9}')

s = '人生苦短，脚本我用 Python'

# 字符串 转 bytes
encode_s = s.encode('utf-8')
print(encode_s)
# base64加密
b64_encode_s = base64.b64encode(encode_s)
print(b64_encode_s)

# base64解密
b64_decode_s = base64.b64decode(b64_encode_s)
# bytes 转 字符串
print(b64_decode_s.decode("utf-8"))


