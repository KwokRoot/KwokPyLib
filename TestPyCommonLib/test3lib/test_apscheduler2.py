# pip install APScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import datetime
import time


class Scheduler:
    def __init__(self):
        self.executors = {
            "default": ThreadPoolExecutor(10),
            "processpool": ProcessPoolExecutor(2)
        }
        # self.scheduler = BackgroundScheduler(executors=self.executors,)
        self.scheduler = BlockingScheduler(executors=self.executors,)

    def getScheduler(self):
        return self.scheduler


def jobs():
    print(datetime.datetime.now())


if __name__ == '__main__':

    sched = Scheduler().getScheduler()
    sched.add_job(jobs, "interval", seconds=1, id="jobs-001")
    sched.start()
    print(sched.get_jobs())

    # # BackgroundScheduler
    # time.sleep(100)

