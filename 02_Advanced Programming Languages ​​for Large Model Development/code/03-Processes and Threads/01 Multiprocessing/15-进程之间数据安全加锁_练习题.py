# 1. 有一个共享变量，存放int，默认值是100000
# 有2个进程，都是对这个变量进行10000次-1操作
# 要求加锁，让最终结果是准确的80000
import multiprocessing as mp
from multiprocessing.synchronize import Lock


def w1(v: mp.Value, lock: Lock):
    for _ in range(10000):
        with lock:
            v.value -= 1
        # lock.acquire()
        # v.value -= 1
        # lock.release()


def w2(v: mp.Value, lock: Lock):
    for _ in range(10000):
        lock.acquire()
        v.value -= 1
        lock.release()


if __name__ == '__main__':
    # lock 创建
    lock = mp.Lock()
    # 共享value
    v = mp.Value('i', 100000)

    w1_process = mp.Process(target=w1, args=(v, lock))
    w2_process = mp.Process(target=w2, args=(v, lock))
    w1_process.start()
    w2_process.start()

    w1_process.join()
    w2_process.join()

    print(v.value)
