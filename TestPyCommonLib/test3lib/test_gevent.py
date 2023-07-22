# gevent：基于协程的 Python 并发库
# 源码：https://github.com/gevent/gevent

# pip install gevent
import gevent

import os
import random
import time


def gevent_a():
    for i in range(5):
        print(i, 'a gevent', os.getpid())
        gevent.sleep(random.random() * 2)
    return 'a gevent result'


def gevent_b():
    for i in range(5):
        print(i, 'b gevent', os.getpid())
        gevent.sleep(random.random() * 2)
    return 'b gevent result'


if __name__ == '__main__':
    start = time.time()

    g_a = gevent.spawn(gevent_a)
    g_b = gevent.spawn(gevent_b)

    gevent_list = [g_a, g_b]
    result = gevent.joinall(gevent_list)
    print(result[0].value)
    print(result[1].value)

    print('->·> spend_time: %f, parent_id: %s' % (time.time() - start, os.getpid()))
