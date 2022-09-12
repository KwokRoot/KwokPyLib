# pip install progressbar
from progressbar import Percentage, Bar, Timer, ETA, FileTransferSpeed, ProgressBar
import time
import sys


total = 100
widgets = ['Progress: ', Percentage(), ' ', Bar('#'), ' ', Timer(), ' ', ETA(), ' ', FileTransferSpeed()]
bar = ProgressBar(widgets=widgets, maxval=total, fd=sys.stdout).start()

for i in range(10):
    time.sleep(1)
    # 设置当前值
    bar.update(10 * i)
    print('')

bar.finish()


