import time


# 升级为带参数的 decorator
def log(prefix='INFO'):
    def log_decorator(f):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            end_time = time.time()
            print('[{}], call {}(), spend_time {:.3f}'.format(prefix, f.__name__, end_time - start_time))
            return result

        return wrapper

    return log_decorator


@log("DEBUG")
def test():
    time.sleep(0.5)
    pass


print(test())


@log()
def test2():
    time.sleep(0.5)
    return "OK"


print(test2())
