# Python `__enter__`、`__exit__` 这两个方法定义了一个上下文管理器对象。
# 当进入 with 块前，__enter__ 被调用并返回一个值（通常是自己），即在`with`代码块之前执行。
# 当退出 with 块后，__exit__ 被调用处理资源的清理（如关闭文件或释放锁），无论`with`代码块是否异常。

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


print("Before with")
with MyContextManager() as m:
    print("Inside the block")
    # raise RuntimeError("测试异常")
print("After with")


'''
输出：
Before with
Entering the context
Inside the block
Exiting the context
After with
'''

