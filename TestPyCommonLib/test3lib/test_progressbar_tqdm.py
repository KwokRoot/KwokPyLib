# pip install tqdm
from tqdm import tqdm
import time
import sys

# 效果
for i in tqdm(range(100), file=sys.stdout):
    time.sleep(0.01)


print("*" * 36, file=sys.stderr)


# 设置增量
bar = tqdm(total=100)
bar.update(30)
time.sleep(1)
bar.update(40)
time.sleep(1)
bar.update(30)

