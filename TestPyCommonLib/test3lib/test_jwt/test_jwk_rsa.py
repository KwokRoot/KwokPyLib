# pip install cryptography
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from cryptography.hazmat.primitives import serialization
import base64


jwks = {
    "keys":
        [
            {
                "kty": "RSA",
                "e": "AQAB",
                "kid": "4e5fe8e2-621d-4e05-9ae1-19003e7f32a7",
                "n": "rB1RrVXHNzv2ezUpi2h8WtXjLUhZu4X8xRS1NYgCqKa03TqQtA6q2g0oofesFi4u6AiAWD-NkHsrB3_2X08T9IoA9dIYd10XO1sdJervL1Hj1yrX78x91xv5TTfxU8EHmEd2bSjdbMwrPhEbKwHb2lD7bdPRmD_12cH7uORLPaGjcGJIjMfJ9LzxaUJkpypRf4gjr2R9BBC7E5giYqaZgHZZhkwYkJHIlSRCJPtyEt_sezF0WJKUAt7yF5eDo8Ox7OZQI__wYRAHq2q-cVuw4vS1CQd_PEL523SvOA1Fn0CXrwvE4UhdHVvS1ovoySbcSGpbOX91BRBEDKwBZuW4sw"
            }
        ]
}
# 根据 jwks 中，`n`, `e` 构建 RSA 公钥
# 一个 RSA 公钥由两个整数构成：
#     n（modulus，模数）：大整数，通常是 2048 位或更长。
#     e（public exponent，公钥指数）：通常为 65537（即 0x10001），Base64Url 编码后是 "AQAB"


def b64_to_int(b64):
    # Base64Url -> int
    b64 = b64.replace('-', '+').replace('_', '/')
    data = base64.b64decode(b64 + '==')
    return int.from_bytes(data, 'big')


key = jwks['keys'][0]
n = b64_to_int(key['n'])
e = b64_to_int(key['e'])

public_numbers = RSAPublicNumbers(e, n)
public_key = public_numbers.public_key()

pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(pem.decode())


if __name__ == '__main__':
    import jwt as py_jwt

    token = "eyJraWQiOiI0ZTVmZThlMi02MjFkLTRlMDUtOWFlMS0xOTAwM2U3ZjMyYTciLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImF1ZCI6ImRlbW8tY2xpZW50IiwibmJmIjoxNzcwNjE1ODg5LCJzY29wZSI6WyJyZWFkIiwib3BlbmlkIiwicHJvZmlsZSIsImVtYWlsIl0sImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTAwMCIsImV4cCI6MTc3MDYxNzY4OSwiaWF0IjoxNzcwNjE1ODg5LCJqdGkiOiIzOTJkMmQ4Mi01YTVjLTQ1NGUtOWY3Yi1jMmFhNDQ4NzJmZDIifQ.QNkiEOz93cWsvXZoy8afhU696PXmB1jr9ivIlnxgPkuTRgg7D24z9Odn9TleeePwn94D5YRXOj8NcqQRM3tB3UK3zQ381NtnAO3t6MwImlnSQ9De1oYcieJjhXBM_uQkziMEdhndic1RWlGsS6hjxDe6xd6KJcUhGiorzYiiwKFdxcam1y4_nSgap1da5dHpABCJuIW4t5FbEi9v5CrCNv6H7emrmmcAlL23SFZJMC9V5zxoNcTN30vaUFr146jjY_eqKLXkUCTRlj9xJ8pgay3vDYTOM1Ztz8ZfqA0F1Q2QAGw4BF2XckiZ1ocZQdtZjAcdYqsCbmqnBb7iMeirmQ"
    decoded = py_jwt.decode(token, pem, algorithms=['RS256'], audience="demo-client")
    print(decoded)


