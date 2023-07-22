# Python中 `@` 装饰器函数，就是通过装饰器函数，在不修改原函数的前提下，来对函数的功能进行合理的扩充。

print(f'{"="*18} 示例 1 {"="*18}')

print(f'{"="*9} 示例 1-1 {"="*9}')


def FX(fn):
    print("*** log-befor ***")
    res = fn()
    print("*** log-after ***")
    return res


def test_x():
    print("test_x")
    return "test_x"


FX(test_x)


print(f'{"="*9} 示例 1-2 {"="*9}')


def FY(fn):
    print("*** log-befor ***")
    res = fn()
    print("*** log-after ***")
    return res


@FY  # @FY 等价于 FY(test_y)
def test_y():
    print("test_y")
    return "test_y"


test_y


print(f'{"="*18} 示例 2 {"="*18}')


def FA(fn):
    def warp():
        return "<a>" + fn() + "<a>"

    return warp


def FB(fn):
    def warp():
        return "<b>" + fn() + "<b>"

    return warp


@FA
def test1():
    return "test1"


@FB
def test2():
    return "test2"


@FA
@FB
def test3():
    return "test3"


print(test1())
# 输出：<a>test1<a>

print(test2())
# 输出：<b>test2<b>

print(test3())
# 输出：<a><b>test3<b><a>


print(f'{"="*13} 示例 3: 传参装饰器 {"="*13}')


def funA(fn):
    def warp(*args, **kwargs):
        fn(*args, **kwargs)

    return warp


@funA
def funB(*args, **kwargs):
    print(f'可变参数: {args}, 关键字参数 {kwargs}')


funB("a", "b", "c", aaa=1, bbb=2)

