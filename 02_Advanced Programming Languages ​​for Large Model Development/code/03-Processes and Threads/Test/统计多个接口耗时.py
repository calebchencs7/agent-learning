"""
背景：
数据平台需要同时请求多个接口，并在所有接口完成后汇总结果。如果一个接口完成后再请求下一个，整体等待时间会比较长。
题目：
使用 asyncio 编写程序，要求：

定义协程函数 request_api(name, delay)，模拟请求接口
函数开始时输出 开始请求：接口名
使用 await asyncio.sleep(delay) 模拟等待
函数结束时返回字符串：接口名完成
在 main() 中同时执行 3 个接口请求
打印所有接口返回结果
"""

import asyncio

# async def request_api(name, delay):
#     print(f"开始请求：{name}")
#     await asyncio.sleep(delay)
#     return f"{name}完成"


# async def main():
#     task1 = asyncio.create_task(request_api("接口A", 1))
#     task2 = asyncio.create_task(request_api("接口B", 2))
#     task3 = asyncio.create_task(request_api("接口C", 3))

#     result1 = await task1
#     result2 = await task2
#     result3 = await task3

#     print(result1, result2, result3)


# if __name__ == "__main__":
#     asyncio.run(main())


async def request_api(name, delay):
    print(f"开始请求：{name}")
    await asyncio.sleep(delay)
    return f"{name}完成"


async def main():
    results = await asyncio.gather(
        request_api("接口A", 1),
        request_api("接口B", 2),
        request_api("接口C", 3),
    )
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
