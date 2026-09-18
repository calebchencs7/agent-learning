import multiprocessing as mp
import time


def work1(num):
    for i in range(10):
        num.value += 1
        print("w1", num.value)
        time.sleep(1)


def work2(num):
    for i in range(10):
        print("w2", num.value)
        time.sleep(1)


if __name__ == '__main__':
    value = mp.Value(
        'i',    # 类型  i int    f float  d double  b bool
        0       # 初始值
    )

    mp.Process(target=work1, args=(value, )).start()
    mp.Process(target=work2, args=(value, )).start()
