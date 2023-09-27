import datetime
import inspect


def func():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# 不同类型的参数定义的顺序：必须参数，默认参数，可变参数，可变关键字参数
def func2(param1, param2, param3=3, *args, **kwargs):
    print(param1, param2, param3, args, kwargs)


# 定义参数类型、返回值类型。注：当 `list[str]` 报 TypeError 异常，可修改为 `typing.List[str]`
def func3(param1: str, param2: list[str], param3: bool = True) -> bool:
    print(f'参数1: {param1}, 参数2: {param2}, 参数3: {param3}')
    return param1 in param2


if __name__ == '__main__':
    func()

    print(func3('hello', ["hello", "word"]))
    # 获取函数名
    print(func3.__name__)
    # 获取函数签名
    signature = inspect.signature(func3)
    print(signature)

