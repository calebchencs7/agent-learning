import numpy as np

# 创建数组
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("原始数组：\n", arr)
print("维度：", arr.ndim)

# 索引 同list
print("第一个元素：", arr[0][0])
print("最后一行：", arr[-1])
print("第二行第二列：", arr[1, 1])     # arr[行, 列]
print("第二列：", arr[:, 1])     # :表示无所谓行
print("第四列：", arr[:, -1])     # :表示无所谓行

# 切片
print("前2行", arr[0: 2])
print("前两行的前2列", arr[0: 2, 0: 2])       # arr[xx, yy]  xx 行的切片0:2   yy 列的切片0: 2
print("前两行的23列", arr[0: 2, 1: 3])
print("前3行的234列", arr[:, 1:])

# 布尔索引
bool_arr = arr > 5
print("布尔结果：\n", bool_arr)

print("----------------")
