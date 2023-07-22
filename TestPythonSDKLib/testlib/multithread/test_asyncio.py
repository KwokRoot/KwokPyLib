import asyncio
import os
import time


async def a():
    for i in range(5):
        print(i, 'a', os.getpid())
        await asyncio.sleep(1)
    return 'a'


async def b():
    for i in range(5):
        await asyncio.sleep(1)
        print(i, 'b', os.getpid())
    return 'b'


async def main():
    result = await asyncio.gather(
        a(),
        b(),
    )
    print(result)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print('->·> spend_time: %f, parent_id: %s' % (time.time() - start, os.getpid()))

