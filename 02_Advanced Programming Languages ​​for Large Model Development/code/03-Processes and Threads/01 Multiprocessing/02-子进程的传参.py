import multiprocessing as mp
import time


def eat(num):
    for i in range(1, num + 1):
        print(f"我吃第{i}次")
        time.sleep(1)


def sleep(num, sec):
    for i in range(1, num + 1):
        print(f"我睡觉觉第{i}次")
        time.sleep(sec)


if __name__ == '__main__':
    # 方式1，位置传参
    # eat_process = mp.Process(
    #     target=eat,
    #     args=(10, )
    # )
    #
    # sleep_process = mp.Process(
    #     target=sleep,
    #     args=(5, 2)
    # )

    # 方式2，关键字传参
    # eat_process = mp.Process(
    #     target=eat,
    #     kwargs={"num": 10}
    # )
    #
    # sleep_process = mp.Process(
    #     target=sleep,
    #     kwargs={"num": 5, "sec": 2}
    # )

    # 方式3，混着来
    eat_process = mp.Process(target=eat, args=(10,))

    sleep_process = mp.Process(target=sleep, kwargs={"num": 5, "sec": 2})

    eat_process.start()
    sleep_process.start()
