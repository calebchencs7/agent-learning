"""
定义函数findall，要求返回符合要求的所有位置的起始下标，
如字符串"helloworldhellopythonhelloc++hellojava"
需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)
"""


def findall(target_str, sub_str):
    """
    查找 target_str 中所有 sub_str 的起始下标，并以元组形式返回
    """
    indices = []
    start = 0

    while True:
        # 从 start 位置开始查找 sub_str 的起始下标
        index = target_str.find(sub_str, start)

        # 找不到时 find 返回 -1，此时跳出循环
        if index == -1:
            break

        indices.append(index)
        # 将下一次搜索的起始位置设置为当前找到位置 + 1（或加上 len(sub_str) 避开重叠匹配）
        start = index + len(sub_str)

    # 将列表转换为元组返回
    return tuple(indices)


# 测试调用
text = "helloworldhellopythonhelloc++hellojava"
result = findall(text, "hello")
print(result)
