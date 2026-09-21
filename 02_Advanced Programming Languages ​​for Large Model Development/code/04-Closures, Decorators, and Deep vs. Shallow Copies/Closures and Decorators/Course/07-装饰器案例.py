# 写一个装饰器，被装饰的函数能够输出执行时间（秒）
import time


def time_clac(fn):
    count = 0  # 便于统计函数被调用多少次

    def inner():
        nonlocal count
        count += 1
        start = time.time()
        fn()
        end = time.time()
        print(f"时间：{end - start:.2f}秒")
        print(count)

    return inner


@time_clac
def compute1():
    for _ in range(1000000):
        1 + 1


@time_clac
def compute2():
    for _ in range(1000000):
        1 + 1
        2 * 2
        num = 3 * 3
        num += 5
        num *= 100


compute1()
compute2()
