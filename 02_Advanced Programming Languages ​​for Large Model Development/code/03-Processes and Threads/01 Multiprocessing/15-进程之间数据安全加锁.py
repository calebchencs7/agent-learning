import multiprocessing as mp
from multiprocessing.synchronize import Lock
import time

"""
上锁解锁
作用是：保证同一时刻只有一个进程能够执行 v.value += 1
执行过程类似于“一个人拿钥匙进入房间”：
进程1拿到锁 → 修改数据 → 释放锁
            ↓
进程2拿到锁 → 修改数据 → 释放锁
"""


def w1(v: mp.Value, lock: Lock):
    for _ in range(100000):
        with lock:  # with lock 进入代码块前自动上锁，离开代码块时自动释放锁。
            v.value += 1


def w2(v: mp.Value, lock: Lock):
    for _ in range(100000):
        lock.acquire()  # 上锁
        v.value += 1
        lock.release()  # 解锁


if __name__ == '__main__':
    v = mp.Value('i', 0)
    lock = mp.Lock()  # Lock()锁对象

    w1_process = mp.Process(target=w1, args=(v, lock))
    w2_process = mp.Process(target=w2, args=(v, lock))

    s = time.time()
    w1_process.start()
    w2_process.start()

    # join等待这个进程运行结束
    w1_process.join()
    w2_process.join()

    e = time.time()
    # 2个子进程结束，下面代码才会执行
    print(f"期望：200000")
    print(f"实际：{v.value}")
    print(f"耗时：{e - s}")
