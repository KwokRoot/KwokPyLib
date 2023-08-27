from package import *
print(a)
print(dir())

# IDE 检查到异常
# print(b)

print(sys.version_info)

import package
print(dir())
print(package.b)


print(package.__path__)
print(sys.path)

