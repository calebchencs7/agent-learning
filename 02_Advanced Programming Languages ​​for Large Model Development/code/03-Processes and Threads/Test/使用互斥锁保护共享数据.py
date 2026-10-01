"""
背景：
电商系统中多个用户可能同时购买同一种商品。如果多个线程同时扣减库存，库存结果可能不准确。下面用简单代码模拟两个线程同时扣库存的场景。
题目：
编写程序模拟两个线程扣减库存，要求：

初始库存 stock = 10。(1分)
定义函数 buy(name, count)，表示某个用户购买 count 件商品。(3分)
使用互斥锁保护库存判断和扣减过程。(3分)
创建三个线程，分别模拟用户购买 3 件、4 件、5 件商品。(2分)
线程结束后打印剩余库存。(1分)
"""

import threading
import time

stock = 10
lock = threading.Lock()


def buy(name, count):
    global stock
    print(f"{name} 准备购买 {count} 件商品")
    with lock:
        if stock >= count:
            stock -= count
            print(f"{name} 成功购买 {count} 件商品，剩余库存 {stock}")
        else:
            print(f"{name} 购买失败，库存不足，剩余库存 {stock}")


# 创建三个线程，分别模拟用户购买 3 件、4 件、5 件商品
threading.Thread(target=buy, args=("用户A", 3)).start()
threading.Thread(target=buy, args=("用户B", 4)).start()
threading.Thread(target=buy, args=("用户C", 5)).start()

print("剩余库存:", stock)
