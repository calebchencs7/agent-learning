import multiprocessing as mp
import time

"""
守护进程：
专门陪着主进程运行的后台子进程；主进程一结束，它也会被强制结束。

# 普通任务：必须执行完
p = mp.Process(target=work)
p.start()
p.join()

# 后台辅助任务：不要求执行完
p = mp.Process(target=work)
p.daemon = True
p.start()

# 通常不对它无限期 join

不过，带超时的 join() 可以和守护进程配合：
p = mp.Process(target=work, daemon=True)
p.start()

p.join(timeout=3) #主进程最多等待子进程 3 秒。

print("主进程准备结束")
"""


def w1():
    for i in range(1, 11):
        print("w1:", i)
        time.sleep(1)


def w2():
    for i in range(100, 111):
        print("w2:", i)
        time.sleep(1)


if __name__ == '__main__':
    mp.Process(target=w1, daemon=True).start()
    mp.Process(target=w2, daemon=True).start()

    time.sleep(2)
    print("主进程现在没代码了，没事干了。")
