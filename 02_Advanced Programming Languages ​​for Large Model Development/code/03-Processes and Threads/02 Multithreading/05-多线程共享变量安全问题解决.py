# 1. 2个线程，线程1对共享变量num += 1   +10000次
# 2. 线程2同样num += 1   + 10000次
# 3. num起始是0
#
# 等待2个线程执行完成后，输出num的最终值（等待线程执行完成，使用线程对象.join()）
import threading

num = 0
count = 10_000_000
lock = threading.Lock()


def w1():
    global num
    for _ in range(count):
        with lock:
            num += 1


def w2():
    global num
    for _ in range(count):
        lock.acquire()
        num += 1
        lock.release()


t1 = threading.Thread(target=w1)
t2 = threading.Thread(target=w2)

t1.start()
t2.start()

# 等待线程执行完成
t1.join()
t2.join()


print(num)
