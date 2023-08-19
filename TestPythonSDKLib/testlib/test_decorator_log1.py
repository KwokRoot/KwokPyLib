import time


def log(f):
    def fn(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print('call ' + f.__name__ + '(), spend_time ' + str(round(end_time - start_time, 3)))
        return result

    return fn


@log
def test():
    time.sleep(0.5)
    return 'test()'
    # pass


print(test())


