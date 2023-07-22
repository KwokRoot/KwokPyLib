import threading
import os
import time
import random

lists = ['python', 'C', 'C++', 'C#', 'java', 'go', 'JavaScript', 'Nodejs', 'PHP']
new_lists = []


def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = '%s_new' % data
    new_lists.append(new_data)
    print(f'>> lists move {data} -> new_lists, {os.getpid()}')
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()

    print('old list len:', len(lists))

    t_list = []
    for i in range(len(lists)):
        t = threading.Thread(target=work)
        t_list.append(t)
        t.start()

    # for t in t_list:
    #     t.join()

    print('old list:', lists)
    print('new list:', new_lists)
    print('new_list len', len(new_lists))
    print('time is %s' % (time.time() - start))

