import multiprocessing as mp
import time

"""
进程之间数据共享问题演示
每个进程都有自己的内存空间，数据不共享
g_list是全局变量，但是每个进程都有自己的g_list，数据不共享  
"""

g_list = []


def increment():
    for i in range(10):
        g_list.append(i)
        print("w1: ", g_list)
        time.sleep(1)


def print_list():
    for _ in range(10):
        print("w2: ", g_list)
        time.sleep(1)


if __name__ == '__main__':
    mp.Process(target=increment).start()
    mp.Process(target=print_list).start()

    for _ in range(10):
        print("Main Process: ", g_list)
        time.sleep(1)
