# simpleeval 是 Python 表达式引擎，相比于 Python 内置的 eval() 函数可以直接执行字符串形式的 Python 表达式，simpleeval 更安全。
# pip install simpleeval
from simpleeval import simple_eval

# 基础数学表达式
result = simple_eval("1 + 2 * (5 - 2)")
print(result)  # 7

# 注入变量
expr_str = "age >= 18 and 'Kuo' in name"
context = {"name": "AndyKuo", "age": 20}
print(simple_eval(expr_str, names=context))  # True


# 自定义函数
def double(x):
    return x * 2


result = simple_eval("double(5) + age", names=context, functions={"double": double})
print(result)  # 30
