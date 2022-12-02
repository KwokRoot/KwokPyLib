import os
import threading


# Python 线程
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(100):
            print(f"{self.name}-{os.getpid()}-{os.getppid()}-{threading.current_thread().name} => {i}")


t1 = MyThread("线程1")
t2 = MyThread("线程2")

t1.start()
t2.start()

