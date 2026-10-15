"""
pandas 是 Python 中专门用于数据分析和数据处理的库。
它特别适合处理类似 Excel 表格或数据库表格的数据，例如：
读取和保存 Excel、CSV 文件
筛选、排序和统计数据
处理缺失值
添加、删除和修改列
分组统计
合并多张表
处理时间序列数据

pandas 中的两个核心数据结构
1. Series：一维数据
Series 可以看成一列数据，类似数据库表中的一列：

2. DataFrame：二维数据
DataFrame 可以看成一个完整的表格：
"""

import pandas as pd

s1 = pd.Series(["a", "b", "c"])
print(s1)
print(type(s1))  # <class 'pandas.Series'>


# 从字典创建
# 字典key作为索引，value作为数据
s2 = pd.Series({"a": 1, "b": 2, "c": 3})
print(s2)
print(type(s2))  # <class 'pandas.Series'>


# 指定索引
"""
["name", "age", "height"] 是索引，相当于行标签；
['caleb', 23, 181] 是这一列中的数据；
索引不会额外增加一个维度。
"""
s3 = pd.Series(['caleb', 23, 181], index=["name", "age", "height"])
print(s3)
print(type(s3))  # <class 'pandas.Series'>
print(s3.ndim)  # 1维
print(s3.shape)  # (3,) 这个一维维度上有 3 个元素

# 取值
print(s3["name"])  # caleb
print(s3.values, type(s3.values))  # ['caleb' 23 181] <class 'numpy.ndarray'>

# 取全部的index
print(s3.index)  # Index(['name', 'age', 'height'], dtype='object')
