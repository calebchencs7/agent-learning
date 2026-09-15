# 需求: for循环实现九九乘法表
# 思路: 外层循环控制行,内层循环控制列
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end="\t")
    # 每一行换行操作
    print()
