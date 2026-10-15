import numpy as np

# 创建示例的数组
arr: np.ndarray = np.array([[1, 2, 3], [4, 5, 6]])

# 属性：ndarray是一个class对象，具有许多属性和方法。以下是一些常用的属性：
print("数组", arr)  # 输出数组
print("数组的形状 (shape):", arr.shape)  # 输出数组的形状
print("数组的维度 (ndim):", arr.ndim)  # 输出数组的维度
print("数组的元素总数 (size):", arr.size)  # 输出数组的元素总数
print("数组的元素类型 (dtype):", arr.dtype)
