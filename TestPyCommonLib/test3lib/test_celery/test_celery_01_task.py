from celery import Celery

from test3lib.test_celery import celery_config

broker = 'redis://:123456@192.168.199.91:6379/11'  # 任务储存
backend = 'redis://:123456@192.168.199.91:6379/12'  # 结果存储，执行完之后结果放在这

# 创建出 Celery 对象
app = Celery(__name__, broker=broker, backend=backend)
app.conf.broker_transport_options = {'global_keyprefix': "celery:"}
app.conf.result_backend_transport_options = {'global_keyprefix': 'celery:'}
app.conf.update(timezone = 'Asia/Shanghai', enable_utc = False)

# 通过 celery 配置获取实例
# app = Celery(__name__)
# app.config_from_object(celery_config)


# 任务通过装饰器 @app.task 进行装饰
# @app.task()
@app.task(name='test3lib.test_celery.test_celery_01_task.add')
# @app.task(name='test_celery_01_task.add')
def add(x, y):
    return x + y


print(app.tasks)


if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO', '--pool=solo']
    app.worker_main(argv=args)
    print(app.tasks)


# 命令行启动 celery worker 任务:
# celery -A test3lib.test_celery.test_celery_01_task worker -l info

# windows 需要加 '-P eventlet'
# celery -A test3lib.test_celery.test_celery_01_task worker -l info --pool=solo
# celery -A test3lib.test_celery.test_celery_01_task worker -l info -P eventlet

