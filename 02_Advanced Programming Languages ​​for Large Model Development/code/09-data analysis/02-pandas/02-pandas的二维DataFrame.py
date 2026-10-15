import pandas as pd

# DataFrame的创建

# 基于字典创建
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '城市': ['北京', '上海', '广州', '深圳'],
    '工资': [5000, 7000, 6000, 8000],
}

df1 = pd.DataFrame(data)
print(df1)
print(type(df1))


# 基于列表
data_list = [
    ['张三', 25, '北京', 5000],
    ['李四', 30, '上海', 7000],
    ['王五', 35, '广州', 6000],
    ['赵六', 28, '深圳', 8000],
]
df2 = pd.DataFrame(data_list)  # 没有列名，列默认0 -> 1 -> 2 -> ...
print(df2)


# 查看DataFrame的基本信息
print("形状：", df1.shape)
print("列名：", df1.columns)  # 列索引
print("索引：", df1.index)  # 行索引
print("数据类型：", df1.dtypes)  # 每个列的类型

print("形状：", df2.shape)
print("列名：", df2.columns)  # 列索引
print("索引：", df2.index)  # 行索引
print("数据类型：", df2.dtypes)  # 每个列的类型
