import sys

'''
`__init__.py`
# Python 3.3 版本之前，定义的 Python Package 下面一定要有 __init__.py 文件，这样 Python 才知道它是一个 package，才可以寻找到相关模块的路径从而被 import。
# Python 3.3 版本之后，无需专门创建一个 `__init__.py` 来告诉 Python 它是一个 package，因为没有 `__init__.py` 目录是 `namespace package`。Python 会自动搜寻 `sys.path` 下所有路径。
'''

'''
`__all__`
# 显式声明了 `__all__`，其他文件中使用 `from 模块名 import *` 导入该模块时，只会导入 `__all__` 列出的成员，其他成员都被排除在外。如果 `__all__` 定义有误，还会明确地抛出异常，方便检查错误。
# 注：
# `__all__` 变量只在以 `from 模块名 import *` 形式导入模块时起作用，而以其他形式，如 `import 模块名`、`from 模块名 import 某成员` 时都不起作用。
# Python 不提倡用 `from 模块名 import *` 这种方式导入。
# 如果一个模块 xxx 没有定义 `__all__`，执行 `from xxx import *` 时会将 xxx 中所有非下划线开头的成员（包括该模块 import 的其他模块成员）都会导入当前命名空间，这样就可能弄脏当前的命名空间。
# 按照 PEP8 建议的风格，__all__ 应该写在所有 import 语句下面，函数、常量等成员定义的上面。
'''

__all__ = [
    "a",
    # "c",  # IDE 检查到异常
    "sys"
]

# 导入 package 自动执行 __init__.py
print(">·>> 导入 package 包")
print(">·>> " + __name__)
print(sys.path)

a = sys.version
b = sys.version_info

