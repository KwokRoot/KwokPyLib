import multiprocessing

import time
import os


def work_a():
    for i in range(10):
        print(i, 'a', os.getpid())
        time.sleep(1)


def work_b():
    for i in range(10):
        print(i, 'b', os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()

    a_p = multiprocessing.Process(target=work_a)  # 子进程1
    # a_p.start()  # 子进程1执行
    # a_p.join()
    b_p = multiprocessing.Process(target=work_b)  # 子进程2
    # b_p.start()  # 子进程2执行
    # b_p.join()

    for p in (a_p, b_p):
        p.start()

    for p in (a_p, b_p):
        p.join()

    for p in (a_p, b_p):
        print(p.is_alive())

    print('->·> spend_time: %f, parent_id: %s' % (time.time() - start, os.getpid()))

