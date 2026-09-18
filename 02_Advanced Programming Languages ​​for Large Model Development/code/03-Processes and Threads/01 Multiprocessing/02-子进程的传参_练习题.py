# 1. 2个子进程，一个子进程，接收1个数字传入，每隔1秒输出数字，输出的数字是1、2、3、... 到传入的数字结束
#
# 2. 子进程2，同样接受一个数字，也是输出1、2、3到传入的数字结束，同时也接受一个name，要求输出数字+name
import multiprocessing as mp
import time


def work1(num):
    for i in range(1, num+1):
        print("work1:", i)
        time.sleep(1)


def work2(num, name):
    for i in range(1, num+1):
        print("work2:", i, name)
        time.sleep(1)


if __name__ == '__main__':
    work1_process = mp.Process(target=work1, args=(10, ))
    work2_process = mp.Process(target=work2, kwargs={"num": 10, "name": "周杰轮"})

    work1_process.start()
    work2_process.start()
