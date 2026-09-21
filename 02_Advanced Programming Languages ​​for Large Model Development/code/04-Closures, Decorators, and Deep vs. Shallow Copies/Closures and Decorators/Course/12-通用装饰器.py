# 装饰器，统计一个函数的执行时长
import time


def time_calc(fn):

    def inner(*args, **kwargs):  # 怎么填，都能收
        # *args ==> 元组
        # **kwargs ==> 字典
        start_t = time.time()
        r = fn(*args, **kwargs)
        end_t = time.time()
        print(f"消耗时间：{end_t - start_t:.2f}秒")
        return r

    return inner


@time_calc
def loop_print(num):
    for i in range(1, num + 1):
        print(i)


@time_calc
def say_hello(name, age, gender):
    print(f"我是{name}，今年{age}岁，性别：{gender}")


@time_calc
def get_sum(num):
    sum_v = 0
    for i in range(1, num + 1):
        sum_v += i

    return sum_v


loop_print(100)
say_hello("周杰轮", 11, "男")
r = get_sum(100)
print(r)
