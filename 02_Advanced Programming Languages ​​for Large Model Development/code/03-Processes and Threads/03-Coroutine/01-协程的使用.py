"""
协程：在一个单进程，单线程的程序中，主动让出CPU的使用权，给其他任务使用CPU的技术
开发的步骤：
1. 给需要交替运行的任务（函数），带上`async`前缀
   1. 在需要移交CPU的地方，调用`await`前缀
2. 创建一个注册函数，在注册函数内，创建协程任务
3. 通过`asyncio.run`启动注册函数即可

"""

# 一个吃 一个睡
import asyncio


async def eat():
    print("我要吃饭了")
    await asyncio.sleep(2)  # 主动移交CPU
    print("吃好了")


async def sleep():
    print("我要睡觉了")
    await asyncio.sleep(5)  # 主动移交CPU
    print("我睡醒了")


async def main():  # 注册任务函数
    # 创建异步任务
    task1 = asyncio.create_task(eat())  # 带括号调用函数
    task2 = asyncio.create_task(sleep())  # 带括号调用函数

    # 启动任务
    await task1
    await task2


asyncio.run(main())
