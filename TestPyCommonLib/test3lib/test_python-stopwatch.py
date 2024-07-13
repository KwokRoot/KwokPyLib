# pip install python-stopwatch
from stopwatch import Stopwatch, profile

import time

stopwatch = Stopwatch()
stopwatch.start()
time.sleep(1.0)
stopwatch.stop()
time.sleep(1.0)
print(stopwatch.elapsed)


print("*" * 36)

with Stopwatch(name='outer') as outer_stopwatch:
    with Stopwatch(name='inner') as inner_stopwatch:
        for i in range(1, 5):
            with inner_stopwatch.lap():
                time.sleep(i / 10)

print(inner_stopwatch.laps)
print(inner_stopwatch.elapsed)
print(inner_stopwatch.report())
print(outer_stopwatch.report())


print("*" * 36)


@profile(name='wait for ts', report_every=None)
def wait_for(ts):
    time.sleep(ts)


wait_for(1)
wait_for(2)
wait_for(3)

