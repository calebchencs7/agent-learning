# 1. 开发2个线程，线程1，每隔1秒输出我在唱歌，输出10次
# 线程2，每隔1秒输出我在吃饭，输出5次
import threading
import time


def sing():
    for _ in range(10):
        print("我唱歌RAP")
        time.sleep(1)


def eat():
    for _ in range(5):
        print("吃着呢")
        time.sleep(1)


# 多线程，不需要写if __name__ == '__main__':
if __name__ == '__main__':
    threading.Thread(target=sing).start()
    threading.Thread(target=eat).start()
