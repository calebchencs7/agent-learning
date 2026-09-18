"""
线程:在已有的进程中可以创建多个执行单元，线程是CPU调度的最小单位，一个进程中可以并发执行多个线程
"""

import time
import threading


def eat():
    print("吃")
    time.sleep(5)
    print("吃完了")


def sleep():
    print("要睡了")
    time.sleep(7)
    print("😴爽了")


if __name__ == '__main__':
    thread_eat = threading.Thread(target=eat, name="吃货线程")
    thread_sleep = threading.Thread(target=sleep, name="😴神线程")

    thread_eat.start()
    thread_sleep.start()

    # 多进程： eat和sleep是可以并行（同时）的（真的是2个CPU核心可以同时跑）
    # 多线程：1个进程不管多少线程，只能同时用1个核心，所以eat和sleep是并发执行（交替）
