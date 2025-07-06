# pip install pyotp
import pyotp

# 生成共享密钥
secret = pyotp.random_base32()
print(f"共享密钥: {secret}")

# 创建 TOTP 对象
totp = pyotp.TOTP(secret, interval=30, digits=6)

# 生成当前验证码
current_code = totp.now()
print(f"当前TOTP验证码: {current_code}")

# 验证验证码
print(f"验证结果: {totp.verify(current_code)}")

# 生成 Provisioning URI (用于生成二维码)
uri = totp.provisioning_uri("user@example.com", issuer_name="MyApp")
print(f"\nProvisioning URI:\n{uri}")


# 通过 secret 获取 TOTP 验证码：
secret = "UOFLP5JOCVUKAYRCSDH6QA7XUAHLLF4A"
totp = pyotp.TOTP(secret, interval=30, digits=6)
print(totp.now())
totp = pyotp.TOTP(secret, interval=30, digits=10)
print(totp.now())

