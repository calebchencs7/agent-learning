#  1. 开发2个进程，一个进程无限循环输出我爱学习，每隔1秒输出1次
# 2. 另一个进程每隔1秒输出，我要吃饭
#
# 注意，创建进程和启动进程的代码，写在if __name__ == '__main__':里面才行
import multiprocessing as mp
import time


def study():
    while True:
        print("我爱学习")
        time.sleep(1)


def eat():
    while True:
        print("我要吃饭")
        time.sleep(1)


if __name__ == '__main__':

    study_process = mp.Process(group=None, target=study, name="学习进程")
    eat_process = mp.Process(group=None, target=eat, name="吃货进程")

    study_process.start()
    eat_process.start()
