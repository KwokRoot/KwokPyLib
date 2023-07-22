import multiprocessing

import os
import time


def work(count, lock):
    lock.acquire()
    print(count, os.getpid())
    time.sleep(1)
    lock.release()
    return 'result is %s, pid is %s' % (count, os.getpid())


if __name__ == '__main__':
    start = time.time()

    pool = multiprocessing.Pool(4)
    manger = multiprocessing.Manager()
    lock = manger.Lock()
    results = []
    for i in range(6):
        result = pool.apply_async(func=work, args=(i, lock))
        results.append(result)

    for res in results:
        print(res.get())

    pool.close()
    pool.join()

    print('->·> spend_time: %f, parent_id: %s' % (time.time() - start, os.getpid()))

