import random
import secrets
import string

# 使用 secrets.choice 来安全地选择列表中的一个随机元素
elements = ['apple', 'banana', 'orange', 'date']
print(secrets.choice(elements))


print("-" * 36)

# 随机密码
print(''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16)))

# 注：secrets 模块默认使用 SystemRandom 作为其随机数生成器，这通常比 random 模块的 Random 类更安全，因为它依赖于系统的随机数生成器。
print(''.join(random.sample(string.ascii_letters + string.digits, 16)))
print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16)))


print("-" * 36)

print(secrets.token_bytes(8))
print(secrets.token_hex(8))
print(secrets.token_urlsafe(8))


print("-" * 36)

print(secrets.randbits(8))
print(secrets.randbelow(100))

