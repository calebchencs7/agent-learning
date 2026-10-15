import numpy as np

# Numpy的核心对象是ndarray对象，需要将数据转换为ndarray对象才能使用Numpy的功能
arr1 = np.array([1, 2, 3])  # 将列表转换为ndarray对象
print(arr1)  # 输出ndarray对象
print(type(arr1))  # 输出ndarray对象的类型


arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 将二维列表转换为ndarray对象
print(arr2)  # 输出ndarray对象
print(type(arr2))  # 输出ndarray对象的类型


# 创建特殊数组
# 全是0的数组
arr3 = np.zeros((3, 4))  # 创建一个3行4列的全是0的数组
print(arr3)  # 输出全是0的数组


# 全是1的数组
arr4 = np.ones((3, 4))  # 创建一个3行4列的全是1的数组
print(arr4)  # 输出全是1的数组


# 创建序列数组
ranger_arr: np.ndarray = np.arange(
    1, 10, 1
)  # 创建一个从1到10（不包括10），步长为1的序列数组
print(ranger_arr)  # 输出序列数组


# 等分数组
linespace_arr: np.ndarray = np.linspace(
    1, 10, 5
)  # 创建一个从1到10（包括10），等分为5份的数组 [ 1.    3.25  5.5   7.75 10.  ]
print(linespace_arr)  # 输出等分数组


# 创建随机数组
random_arr: np.ndarray = np.random.rand(
    3, 4
)  # 创建一个3行4列的随机数组，数组中的值服从[0, 1)的均匀分布
print(random_arr)  # 输出随机数组


# 标准正态分布的数组
random_normal_arr: np.ndarray = np.random.randn(
    3, 4
)  # 创建一个3行4列的随机数组，数组中的值服从标准正态分布
print(random_normal_arr)  # 输出标准正态分布的随机数组
