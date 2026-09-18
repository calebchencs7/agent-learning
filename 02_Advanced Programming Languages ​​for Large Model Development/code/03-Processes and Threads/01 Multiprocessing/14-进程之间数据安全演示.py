import multiprocessing as mp
import time

"""
两个进程可能同时读取同一个旧值：
假设当前值为 100

进程 w1 读取：100
进程 w2 读取：100

进程 w1 计算：101
进程 w2 计算：101

进程 w1 写入：101
进程 w2 写入：101
进行了两次加一，结果却只从 100 变成了 101，有一次修改被覆盖了。这叫：
- 数据竞争
- 竞态条件
"""


def w1(v: mp.Value):
    for _ in range(100000):
        v.value += 1


def w2(v: mp.Value):
    for _ in range(100000):
        v.value += 1


if __name__ == '__main__':
    v = mp.Value('i', 0)
    w1_process = mp.Process(target=w1, args=(v,))
    w2_process = mp.Process(target=w2, args=(v,))

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
