import getpass

password = input("请输入密码: ")
print(password)

# 不显示输入内容，控制台下有效
password = getpass.getpass("请输入密码: ")
print(password)
