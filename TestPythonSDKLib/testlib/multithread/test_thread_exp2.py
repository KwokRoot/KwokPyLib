import threading


class MyThread(threading.Thread):
    def __init__(self, thread_name, args):
        super(MyThread, self).__init__(name=thread_name)
        self.args = args

    def run(self):
        print(f'{threading.current_thread().name} : {self.args[0]}')


if __name__ == '__main__':
    for i in range(10):
        MyThread(thread_name=f"T1-{i}", args=[i]).start()


