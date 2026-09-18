# 1. 创建一个Value类对象在2个进程之间共享
# 2. 进程1每隔2秒，将共享Value - 1
# 3. 进程2 每隔2秒，print共享的Value
#
# 4. Value初始值为100
import multiprocessing as mp
import time


def work1(share_value):
    for _ in range(10):
        share_value.value -= 1
        time.sleep(2)


def work2(share_value):
    for _ in range(10):
        print(f"共享变量：{share_value.value}")
        time.sleep(1)


if __name__ == '__main__':
    share_value = mp.Value("i", 10)
    p1 = mp.Process(target=work1, args=(share_value,))
    p2 = mp.Process(target=work2, args=(share_value,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
