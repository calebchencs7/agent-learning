"""
创建一个新的内存空间，提供给一个独立的程序使用
"""

import multiprocessing
import time


def eat():  # 函数：进程要做的工作
    for _ in range(10000000):
        print("吃吃吃")
        time.sleep(3)


def sleep():  # 函数：进程要做的工作
    for _ in range(10000000):
        print("睡睡睡")
        time.sleep(3)


if __name__ == '__main__':
    process_eat = multiprocessing.Process(
        group=None,  # group 固定为None（Python官方预留的参数，以后可能更新）
        target=eat,  # target目标，这个进程要执行什么代码，传入一个函数名
        name="吃😏",  # 给创建的这个进程起个名字
    )

    process_sleep = multiprocessing.Process(
        group=None,  # group 固定为None（Python官方预留的参数，以后可能更新）
        target=sleep,  # target目标，这个进程要执行什么代码，传入一个函数名
        name="睡😴",  # 给创建的这个进程起个名字
    )

    process_eat.start()  # 创建此进程开始干活
    process_sleep.start()  # 创建此进程开始干活

    print("asdsaaaaaaaaaaaaaaaaaaa")
