from test3lib.test_celery.test_celery_01_task import add
# from test_celery_01_task import add


# 添加异步任务，返回一个 AsyncResult 实例，可以用于进行跟踪任务状况
# result = add.delay(3, 4)
result = add.apply_async(args=(3, 4))
print(result)
print(type(result))

print(result.backend)

print(result.ready())

# 如果任务出现异常，可以通过以下命令进行回溯
print(result.traceback)

# 是否正常执行完成,正常执行成功返回 True，否则返回 False
print(result.successful())

# 是否正常执行失败,失败返回 True，否则返回 False
print(result.failed())

# 查看任务状态，执行状态 PENDING、RETRY、STARTED
print(result.status)

# 执行成功打印结果
print(result.get())


