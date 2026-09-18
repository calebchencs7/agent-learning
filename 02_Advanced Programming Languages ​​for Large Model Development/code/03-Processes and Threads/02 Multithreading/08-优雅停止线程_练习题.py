# 写1个线程，无限循环每隔1秒输出信息（内容随意），
# 要求，主线程内无限循环得到随机数，如果随机数是5，则停止线程
import threading
import time
import random

flag = True


def work1():
    while flag:
        print("工作1")
        time.sleep(1)


if __name__ == '__main__':
    threading.Thread(target=work1).start()

    while True:
        random_num = random.randint(1, 10)
        print(f"随机数：{random_num}")

        if random_num == 5:
            # 停止work1线程
            flag = False
            break

        time.sleep(0.5)
