import threading
import time

import psutil
# pip install uvicorn
import uvicorn
# pip install fastapi
from fastapi import FastAPI

app = FastAPI()


# http://127.0.0.1:11110/status
@app.get("/status")
def get_status():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    }


def start_monitor(port):
    uvicorn.run(app, host="0.0.0.0", port=11110)


if __name__ == "__main__":
    monitor_thread = threading.Thread(target=start_monitor, args=(11110,))
    monitor_thread.start()
    print("监控端口已开启")

    # 业务代码逻辑
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(3)

