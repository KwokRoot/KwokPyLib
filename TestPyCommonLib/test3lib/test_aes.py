# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 定义 Key
key = "21232f297a57a5a743894a0e4a801fc3"
# 定义编码字符集
ENCODING = "utf-8"

cipher = AES.new(key.encode(ENCODING), AES.MODE_ECB)

# 加密
# ValueError: Data must be aligned to block boundary in ECB mode 异常：需使用 pad() 方法填充
encrypt_byte = cipher.encrypt(pad("hello world. 中国".encode(), AES.block_size, "pkcs7"))
encrypt_str = base64.b64encode(encrypt_byte).decode(ENCODING)
print(encrypt_str)


# 解密
b64decode_byte = base64.b64decode(encrypt_str.encode(ENCODING))
decode_byte = cipher.decrypt(b64decode_byte)
decrypt_str = unpad(decode_byte, AES.block_size, "pkcs7").decode()

print(decrypt_str)


