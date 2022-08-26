import time

import schedule


def print_time():
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        x = 10/0
    except Exception as e:
        print(e)
        pass


schedule.every(3).seconds.do(print_time)

while True:
    schedule.run_pending()

