import multiprocessing as mp
import time


def w1():
    while True:
        print("w1:")
        time.sleep(1)


def w2():

    while True:
        print("w2:")
        time.sleep(1)
        # 子进程自己结束自己
        # print("w2 自己结束")
        # return


if __name__ == '__main__':
    w1_process = mp.Process(target=w1)
    w2_process = mp.Process(target=w2)

    w1_process.start()
    w2_process.start()

    time.sleep(2)
    print("主进程现在没代码了，没事干了。杀掉2个小弟")

    w1_process.terminate()
    w2_process.terminate()

    print("2个小弟干掉了")
