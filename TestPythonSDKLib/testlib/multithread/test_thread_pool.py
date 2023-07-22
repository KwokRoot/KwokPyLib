from concurrent.futures import ThreadPoolExecutor

import time
import os


def work(i):
    print(i, f', pid: {os.getpid()}')
    time.sleep(1)
    return 'result %s' % i


if __name__ == '__main__':
    start = time.time()

    t = ThreadPoolExecutor(2)
    result = []
    for i in range(5):
        t_result = t.submit(work, (i, ))
        result.append(t_result)

    # for res in result:
    #     print(res.result())

    print('->·> spend_time: %f, pid: %s' % (time.time() - start, os.getpid()))

