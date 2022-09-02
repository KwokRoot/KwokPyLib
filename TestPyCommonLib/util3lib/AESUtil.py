# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

'''
AES 工具类：使用 ECB 模式加密，pkcs7 格式的 padding
'''


class AESUtil:

    # 使用 ECB 模式加密
    MODE = AES.MODE_ECB
    # 使用默认 pkcs7 padding
    PAD_STYLE = 'pkcs7'
    # 定义编码字符集
    ENCODING = 'UTF-8'

    # key 长度只能为 16 或 24 或 32，分别对应 AES-128、 AES-192、AES-256
    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        # 将密钥编码为 UTF-8 格式的 bytes
        key_bytes = key.encode(AESUtil.ENCODING)
        # 创建 AES 对象
        cipher = AES.new(key_bytes, AESUtil.MODE)
        # 将明文编码为 UTF-8 格式的 bytes
        plaintext_bytes = plaintext.encode(AESUtil.ENCODING)
        # 为编码后的明文添加 padding
        plaintext_bytes_padded = pad(plaintext_bytes, AES.block_size, AESUtil.PAD_STYLE)
        # 执行加密
        ciphertext_bytes = cipher.encrypt(plaintext_bytes_padded)
        # 将加密后的 bytes 进行 base64 编码
        # 注意：不能用 encodebytes！否则会每 76 个字符增加一个换行符，见：https://docs.python.org/zh-cn/3/library/base64.html
        ciphertext_base64_bytes = base64.b64encode(ciphertext_bytes)
        # 将 base64 编码过的 bytes，解码为 Python 中使用的字符串类型
        ciphertext = ciphertext_base64_bytes.decode(AESUtil.ENCODING)
        return ciphertext

    @staticmethod
    def decrypt(ciphertext: str, key: str) -> str:
        # 将密钥编码为 UTF-8 格式的 bytes
        key_bytes = key.encode(AESUtil.ENCODING)
        # 创建 AES 对象
        decrypter = AES.new(key_bytes, AESUtil.MODE)
        # 将密文编码为 UTF-8 格式的（同时也是 base64 编码的）bytes
        ciphertext_base64_bytes = ciphertext.encode(AESUtil.ENCODING)
        # 将 base64 编码的 bytes，解码为原始的密文 bytes
        ciphertext_bytes = base64.b64decode(ciphertext_base64_bytes)
        # 解码为明文
        plaintext_bytes_padded = decrypter.decrypt(ciphertext_bytes)
        # 去掉 Padding
        plaintext_bytes = unpad(plaintext_bytes_padded, AES.block_size, AESUtil.PAD_STYLE)
        # 将 UTF-8 格式编码的明文 bytes，解码为 Python 中的字符串类型
        plaintext = plaintext_bytes.decode(AESUtil.ENCODING)
        return plaintext


if __name__ == '__main__':

    key_str32 = "21232f297a57a5a743894a0e4a801fc3"

    encrypt_str = AESUtil.encrypt("hello world.", key_str32)
    print(encrypt_str)

    decrypt_str = AESUtil.decrypt(encrypt_str, key_str32)
    print(decrypt_str)


