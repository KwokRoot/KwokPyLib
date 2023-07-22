
def test_try():
    try:
        print("执行异常前代码")

        # 抛异常后的 try 代码块不会执行
        # raise FileExistsError("自定义抛异常")
        # print("执行异常后代码")

        # 断言
        # assert 1 > 2, "断言不成立"

        return "try"

    except (FileExistsError, Exception) as e:
        print("有异常执行的代码", e)
        # exit(-1)
        return "except"

    else:
        print("无异常执行的代码")
        return "else"

    finally:
        print("有无异常都会执行的代码")
        # try、except、finally 中都有 return 时，finally 中 return 值《会》覆盖 try、except 中 return 值。
        return "finally"


print('result: %s' % test_try())


