# TTL：Time To Live     # 剩余存活时间
import threading
import time

# 1. 线程：作为计时器
# 2. 其它线程读取计时器的值，超时自我了结

time_counter = 0


# def timer():
#     global time_counter
#     while True:
#         time.sleep(1)
#         time_counter += 1


def work():
    start_time = time.time()

    while True:
        print("我爱工作。")
        time.sleep(1)
        # 直接使用时间差来判断是否超时
        if time.time() - start_time > 5:
            print("工作结束回家睡觉")
            break


# threading.Thread(target=timer).start()
threading.Thread(target=work).start()
