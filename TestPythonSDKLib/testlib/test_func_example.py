print(f'{"*" * 9} 示例1 {"*" * 9}')


# 注：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def func1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = func1()
print(f1(), f2(), f3())
# 结果：9 9 9
# 原因：当 func1() 函数返回了 3个 函数时，f1、f2、f3 并没有被调用，此时他们并未计算 `i * i`。
# 当执行这 3个 函数时，引用的变量 i 的值已经变成了 3。
# 注：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


print(f'{"*" * 9} 示例2 {"*" * 9}')


# 懒计算
# 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
def calc_sum(list_):
    def lazy_sum():
        return sum(list_)
    return lazy_sum


print(calc_sum([1, 2, 3]))
print(calc_sum([1, 2, 3])())


