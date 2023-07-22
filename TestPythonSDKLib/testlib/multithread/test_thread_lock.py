import threading
from concurrent.futures import ThreadPoolExecutor

import os
import time


lock = threading.Lock()


def work(i):
    lock.acquire()
    print(i, f', pid: {os.getpid()}')
    time.sleep(1)
    lock.release()
    return 'result %s' % i


if __name__ == '__main__':
    start = time.time()

    t = ThreadPoolExecutor(2)
    result = []
    for i in range(5):
        res = t.submit(work, (i,))
        result.append(res)

    # for r in result:
    #     print(r.result())

    print('->·> spend_time: %f, parent_id: %s' % (time.time() - start, os.getpid()))

