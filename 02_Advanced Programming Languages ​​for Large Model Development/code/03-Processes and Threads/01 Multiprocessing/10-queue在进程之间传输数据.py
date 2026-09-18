"""
进程1，每隔1秒生成一个随机数
    向队列添加 put
进程2，得到进程1生成的随机数，判断是奇数还是偶数输出
    从队列取出 get
"""

import multiprocessing as mp
import time
import random


def w1(q):
    for _ in range(10):
        num = random.randint(1, 1000)
        q.put(num)
        print(f"w1放入：{num}")
        time.sleep(1)

    # 数据生产结束
    q.put(None)  # 向队列中放入None，表示数据生产结束


def w2(q):
    while True:
        num = q.get()  # q.get()是阻塞的，如果队列为空，进程会一直等待，直到队列中有数据
        if num is None:  # 如果取到None，说明w1已经结束了
            break  # break out of the loop and end the process

        if num % 2 == 0:
            print(f"w2，偶数：{num}")
        else:
            print(f"w2，奇数：{num}")
    print("w2 处理结束")


if __name__ == '__main__':
    q = mp.Queue()  # 不是Python内置的queue包，而是用multiprocessing包内的Queue
    p1 = mp.Process(target=w1, args=(q,))
    p2 = mp.Process(target=w2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主进程结束")
