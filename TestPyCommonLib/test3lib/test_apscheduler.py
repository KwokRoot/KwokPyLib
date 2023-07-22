# python 定时任务框架 APscheduler(Advanced Python Scheduler)
# pip install APScheduler

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def my_job(info):
    print("{}: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), info))


scheduler = BlockingScheduler()

# trigger: date
scheduler.add_job(my_job, 'date', run_date=datetime(2023, 7, 20, 11, 00, 0), args=['测试'])

# trigger: interval
# scheduler.add_job(my_job, 'interval', seconds=1, args=['info'])

# trigger: cron
# scheduler .add_job(my_job, 'cron', second="*", args=["info"])

scheduler.start()

