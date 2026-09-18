"""
Python没有提供线程的terminate()方法
一般通过标志位完成
"""
import time
import threading

flag = True


def work():
    while flag:
        print("我爱工作，工作使我强大，让我成为牛马!!!")
        time.sleep(1)
    print("work线程停止")


if __name__ == '__main__':

    t1 = threading.Thread(target=work)
    t1.start()

    time.sleep(5)
    print("公司黄了，你别干活了")
    flag = False
