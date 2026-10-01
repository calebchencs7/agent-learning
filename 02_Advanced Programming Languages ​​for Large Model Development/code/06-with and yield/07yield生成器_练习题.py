# 写一个函数搭配yield得到生成器
#
# 生成的规则是，随机提供10个数字（范围1-100）
import random


def my_generator():
    for _ in range(10):
        yield random.randint(1, 100)


gen = my_generator()
for num in gen:
    print(num)
