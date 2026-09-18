# 1. 创建2个子进程，内容随意
#  2. 在子进程1和2通过multiprocessing模块打印子进程1的pid和name
#
# 3. 在主进程代码中，用os模块获取pid和ppid并print出来
import multiprocessing as mp
import os


def work1():
    process = mp.current_process()
    pid = process.pid
    name = process.name

    print(f"子进程{name}的pid是{pid}")

    print("work1结束")


def work2():
    process = mp.current_process()
    pid = process.pid
    name = process.name

    print(f"子进程{name}的pid是{pid}")

    print("work2结束")


if __name__ == '__main__':
    pid = os.getpid()
    ppid = os.getppid()
    print(f"主进程MainProcess的pid：{pid}，ppid：{ppid}")

    # work1_process = mp.Process(target=work1, name="工人1")
    # work2_process = mp.Process(target=work2, name="工人2")
    # work1_process.start()
    # work2_process.start()

    mp.Process(target=work1, name="工人1").start()
    mp.Process(target=work2, name="工人2").start()

    print("asdasd")
