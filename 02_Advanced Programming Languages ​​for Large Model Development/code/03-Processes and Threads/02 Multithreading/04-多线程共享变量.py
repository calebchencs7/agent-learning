# 进程之间，内存隔离。线程（同进程的）之间，内存共享
import threading
import time

g_list = []


def w1():
    for _ in range(10):
        g_list.append(1)
        print("w1", g_list)
        time.sleep(1)


def w2():
    for _ in range(10):
        print("w2", g_list)
        time.sleep(1)


threading.Thread(target=w1).start()
threading.Thread(target=w2).start()
