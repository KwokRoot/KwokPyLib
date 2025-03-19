import threading


def exe(arg1):
    print(f'{threading.current_thread().name} : {arg1}')


if __name__ == '__main__':
    for i in range(10):

        threading.Thread(target=exe, name=f"T1-{i}", args=[i]).start()

        # 以下错误写法(实则为主进程执行：MainThread)，target 值为调用的函数名，不能加括号！
        threading.Thread(target=exe(i), name=f"T2-{i}").start()

