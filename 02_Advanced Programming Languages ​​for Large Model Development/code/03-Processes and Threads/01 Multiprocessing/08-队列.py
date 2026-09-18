g_list = []

# 模拟放入队列
for i in range(1, 11):
    g_list.append(i)
    print("放入队列", i)
print(f"队列剩余元素：{g_list}")  # 队列剩余元素：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(
        "取出队列", g_list.pop(0)
    )  # pop按照下标取出，pop(0)表示取出第一个元素，并且删除该元素
print(f"队列剩余元素：{g_list}")  # 队列剩余元素：[]
