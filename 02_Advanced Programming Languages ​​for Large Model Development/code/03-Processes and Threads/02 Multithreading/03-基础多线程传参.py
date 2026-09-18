import time
import threading


def eat(sec):
    print("吃")
    time.sleep(sec)
    print("吃完了")


def sleep(sec, name):
    print(f"{name}要睡了")
    time.sleep(sec)
    print(f"{name}😴爽了")


if __name__ == '__main__':
    thread_eat = threading.Thread(target=eat, name="吃货线程", args=(5, ))
    thread_sleep = threading.Thread(target=sleep, name="😴神线程", kwargs={"sec": 7, "name": "王力宏"})

    thread_eat.start()
    thread_sleep.start()

    # 多进程： eat和sleep是可以并行（同时）的（真的是2个CPU核心可以同时跑）
    # 多线程：1个进程不管多少线程，只能同时用1个核心，所以eat和sleep是并发执行（交替）
