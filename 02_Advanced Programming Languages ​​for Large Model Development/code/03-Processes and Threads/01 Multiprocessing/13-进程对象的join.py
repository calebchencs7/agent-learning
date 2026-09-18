import multiprocessing as mp
import time


def w1():
    for _ in range(5):
        print("w1:")
        time.sleep(1)


def w2():
    for _ in range(10):
        print("w2:")
        time.sleep(1)


if __name__ == '__main__':
    w1_process = mp.Process(target=w1)
    w2_process = mp.Process(target=w2)

    w1_process.start()
    w2_process.start()

    # 必须2个子进程执行完成，才执行下面的代码
    w1_process.join()       # 卡住，直到w1子进程执行结束
    print("w1结束")
    w2_process.join()       # 卡住，直到w2子进程执行结束
    print("w2结束")

    print("主进程没代码啦")


