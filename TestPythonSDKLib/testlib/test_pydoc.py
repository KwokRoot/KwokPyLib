# Python 语法提示基础
import pydoc

obj = list([])

# 获取对象类型
print(type(obj))

# 获取对象的属性及方法
print(dir(obj))

# 获取对象的属性及方法，并标识属性及方法。
print([(name, type(getattr(obj, name))) for name in dir(obj)])

# 获取对象的属性及方法，并标识属性及方法。
print([(name, 'func' if callable(getattr(obj, name)) else 'attr') for name in dir(obj)])


# 打印 `pydoc` 帮助信息，获取属性及方法的说明文档。

help(obj)

print("*" * 36)

help(obj.pop)

print("*" * 36)

help("open")

print("*" * 36)

pydoc.help("pydoc")


