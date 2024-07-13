# pip install dill
import dill

# pip install joblib
import joblib

import pickle


# Python 序列化类库。
# 常见的序列化库有 `pickle`、`joblib`、`dill` 库。
# `dill` 不仅能够序列化 pickle 所能处理的对象，还能处理函数、类、Lambda表达式 等复杂对象。


# 定义一个简单的函数
def hello(name):
    return f"Hello, {name}!"


# 序列化函数对象到文件
with open('hello.pkl', 'wb') as f:
    dill.dump(hello, f)


# 从文件中反序列化函数对象
with open('hello.pkl', 'rb') as f:
    hello1 = dill.load(f)

# 调用反序列化的函数
print(hello1('World'))  # 输出: Hello, World!


# 序列化函数对象到文件
with open('hello.bin', 'wb') as f:
    pickle.dump(hello, f)


# 从文件中反序列化函数对象
with open('hello.bin', 'rb') as f:
    hello2 = pickle.load(f)

# 调用反序列化的函数
print(hello2('World'))  # 输出: Hello, World!


# 序列化函数对象到文件
with open('hello.x', 'wb') as f:
    joblib.dump(hello, f)


# 从文件中反序列化函数对象
with open('hello.x', 'rb') as f:
    hello3 = joblib.load(f)

# 调用反序列化的函数
print(hello3('World'))  # 输出: Hello, World!

