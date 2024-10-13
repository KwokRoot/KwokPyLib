# pip install pycrypto
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.Hash import SHA

import base64
import traceback


def generate_key():
    # 伪随机数生成器
    random_generator = Random.new().read
    # rsa 算法生成实例
    rsa = RSA.generate(2048, random_generator)

    # 导出私钥
    private_pem = rsa.exportKey()
    with open("temp/private_key.pem", "wb") as f:
        f.write(private_pem)

    # 导出公钥
    public_pem = rsa.publickey().exportKey()
    with open("temp/public_key.pem", "wb") as f:
        f.write(public_pem)


# rsa 加密
def rsa_encrypt(rsa_key, mingwen):
    # 创建用于执行pkcs1_v1_5加密或解密的密码
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    miwen_byte = cipher.encrypt(mingwen.encode("utf-8"))
    miwen_text = base64.b64encode(miwen_byte)
    return miwen_text.decode("utf-8")


# rsa 解密
def rsa_decrypt(rsa_key, miwen_text):
    miwen_byte = base64.b64decode(miwen_text)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    mingwen_byte = cipher.decrypt(miwen_byte, b"rsa")
    return mingwen_byte.decode("utf-8")


# 私钥签名
def rsa_sign(rsa_private_key, origin_text):
    signer = Signature_pkcs1_v1_5.new(rsa_private_key)
    digest = SHA.new()
    digest.update(origin_text.encode("utf-8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    return signature.decode("utf-8")


# 公钥验签
def rsa_sign_verify(rsa_public_key, origin_text, sign_text):
    verifier = Signature_pkcs1_v1_5.new(rsa_public_key)
    digest = SHA.new()
    digest.update(origin_text.encode("utf-8"))
    is_verify = verifier.verify(digest, base64.b64decode(sign_text))
    return is_verify


if __name__ == '__main__':

    # 生成密钥，储存
    # generate_key()

    # 读取私钥
    private_key = open('temp/private_key.pem', 'r').read()
    rsa_private_key = RSA.importKey(private_key)

    # 读取公钥
    public_key = open('temp/public_key.pem', 'r').read()
    rsa_public_key = RSA.importKey(public_key)

    mingwen = "helloworld"

    # 公钥加密，私钥解密
    miwen = rsa_encrypt(rsa_public_key, mingwen)
    print(miwen)

    print(rsa_decrypt(rsa_private_key, miwen))

    # 私钥加密，公钥解密
    miwen = rsa_encrypt(rsa_private_key, mingwen)
    print(miwen)
    try:
        print(rsa_decrypt(rsa_public_key, miwen))
    except Exception as e:
        traceback.print_exc()
        print("ERROR: 私钥加密，公钥解密(不支持)，会异常：This is not a private key")

    # 私钥签名，公钥验签
    sign_mingwen = rsa_sign(rsa_private_key, mingwen)
    print(sign_mingwen)

    is_verify = rsa_sign_verify(rsa_public_key, mingwen, sign_mingwen)
    print(is_verify)
