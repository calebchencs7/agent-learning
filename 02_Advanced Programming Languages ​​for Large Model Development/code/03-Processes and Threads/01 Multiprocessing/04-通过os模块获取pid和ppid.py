import multiprocessing
import multiprocessing as mp
import time
import os  # os -> operating system 操作系统


def work1(num):
    # 得到work1进程的pid和ppid
    pid = os.getpid()  # 获取到当前进程的pid
    ppid = os.getppid()  # 获取到当前进程的父进程的pid
    print(f"子进程work1的pid：{pid}")
    print(f"子进程work1的ppid：{ppid}")

    for i in range(1, num + 1):
        print("work1:", i)
        time.sleep(1)


def work2(num, name):
    # 得到work2进程的pid和ppid
    pid = os.getpid()
    ppid = os.getppid()
    print(f"子进程work2的pid：{pid}")
    print(f"子进程work2的ppid：{ppid}")

    for i in range(1, num + 1):
        print("work2:", i, name)
        time.sleep(1)


if __name__ == '__main__':
    # 得到主进程的pid和ppid
    pid = os.getpid()
    ppid = os.getppid()
    print(f"主进程MainProcess的pid：{pid}")
    print(f"主进程MainProcess的ppid：{ppid}")

    work1_process = mp.Process(target=work1, name="work1", args=(1000000,))
    work2_process = mp.Process(
        target=work2, name="work2", kwargs={"num": 1000000, "name": "周杰轮"}
    )

    work1_process.start()
    work2_process.start()
