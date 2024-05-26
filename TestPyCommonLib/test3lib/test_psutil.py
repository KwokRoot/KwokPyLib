# pip install psutil
import psutil

# 进程信息
# pids = psutil.pids()
# for pid in pids:
#     p = psutil.Process(pid)
#     print(f'{p.name()} {p.memory_percent()} {p.cpu_percent()}')

# cpu
print(psutil.cpu_percent(interval=10, percpu=False))

# 内存
print(psutil.virtual_memory())

# 缓存
print(psutil.swap_memory())

# 磁盘
disk_parts = psutil.disk_partitions()
for disk_part in disk_parts:
    opts = disk_part.opts
    # print(disk_part)
    if not opts in ["cdrom"]:
        print(f"{disk_part.mountpoint} {psutil.disk_usage(disk_part.mountpoint)}")

