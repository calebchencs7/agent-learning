import queue

# 创建一个先进先出队列对象
q = queue.Queue(10)  # 队列最大长度为10，如果不指定，默认是无限长度（看内存）

# 向队列中添加元素，尾部入列
for i in range(1, 11):
    q.put(i)
    print(f"入队元素: {i}")

# 打印队列当前元素
print(f"队列当前元素: {list(q.queue)}")


# 从队列中取出元素，头部出列
while not q.empty():
    print(f"出队元素: {q.get()}")

# 打印队列当前元素
print(f"队列当前元素: {list(q.queue)}")
# 队列大小
print(f"队列大小: {q.qsize()}")
