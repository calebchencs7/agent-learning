# 1. 2个进程，  进程1 负责向队列内每隔1秒放入一个随机数字
# 2. 进程2从队列取出，将数字乘以10后print
import multiprocessing as mp
import time
import random


def w1(q):
    for _ in range(10):
        num = random.randint(1, 100)
        q.put(num)  # 放入队列
        print(f"放入num：{num}")
        time.sleep(1)
    q.put(None)  # 放入一个None作为结束标志


def w2(q):
    while True:
        num = q.get()  # 阻塞等待
        if num is None:
            break
        print(f"处理后的num：{num * 10}")


if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=w1, args=(q,))
    p2 = mp.Process(target=w2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
