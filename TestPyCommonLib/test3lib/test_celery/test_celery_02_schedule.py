import datetime

from celery import Celery
from celery.schedules import crontab

# 通过 celery 配置获取实例
from test3lib.test_celery import celery_config


app = Celery(__name__)
app.config_from_object(celery_config)


# @app.task(name="test3lib.test_celery.test_celery_02_schedule.task1")
@app.task()
def task1(*args, **kwargs):
    print(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))
    return datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")


print(app.tasks)


app.conf.beat_schedule = {
    'monitor-heartbeat1': {
        'task': 'test3lib.test_celery.test_celery_02_schedule.task1',
        'schedule': datetime.timedelta(seconds=3),
        'args': (),
    },
    'monitor-heartbeat2': {
        'task': 'test3lib.test_celery.test_celery_02_schedule.task1',
        'schedule': crontab(minute="*/1"),
        'args': (),
    },
}


# 命令行启动 celery 定时任务:
# celery -A test3lib.test_celery.test_celery_02_schedule beat -l info
# celery -A test3lib.test_celery.test_celery_02_schedule worker -l info -P eventlet

