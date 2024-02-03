# #生成名字、地址、电话号码等各种类型的伪数据，填充测试数据库。
# pip install Faker
from faker import Faker


# 'zh_CN', 'en_US', 'ja_JP'
fake = Faker('zh_CN')

# 为了在多次生成数据时保持一致性，使用 seed() 方法来给随机数生成器设置一个种子
Faker.seed(4321)

# 生成一个姓名
print(fake.name())

# 生成一个地址
print(fake.address())

# 生成一个手机号
print(fake.phone_number())

# 生成一段文本
print(fake.text())

# 生成 10 个不同的姓名
for _ in range(10):
    print(f'{fake.name()}: {fake.address()}')

