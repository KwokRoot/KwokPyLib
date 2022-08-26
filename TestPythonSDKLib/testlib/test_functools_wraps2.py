from time import time, sleep
from functools import wraps


def timer(func):

    @wraps(func)
    def new_func(*args, **kwargs):
        start = time()
        ret = func(*args, **kwargs)
        duration = time() - start
        print('总共运行了', duration)
        return ret
    return new_func


@timer
def do_sleep(sec):
    sleep(sec)


do_sleep(2)

print(do_sleep.__name__)
