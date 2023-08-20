import datetime


def func():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# 不同类型的参数定义的顺序：必须参数，默认参数，可变参数，可变关键字参数
def func2(param1, param2, param3=3, *args, **kwargs):
    print(param1, param2, param3, args, kwargs)


if __name__ == '__main__':
    func()


