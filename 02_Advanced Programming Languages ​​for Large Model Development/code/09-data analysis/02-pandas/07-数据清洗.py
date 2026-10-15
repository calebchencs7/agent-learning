import pandas as pd

# 读取csv
# df = pd.read_csv("../data/test.csv", sep="|")
df = pd.read_csv("../data/清洗数据.csv", sep=",")  # 分隔符是啥，不填默认认为是,
print(df)

print("\n缺失值统计")
print(df.isnull().sum())

print("\n非缺失值统计")
print(df.notnull().sum())

print("\n删除含有缺失值的行")
print(df.dropna())  # na 表示缺失

print("\n删除全部都是缺失值的行")
print(df.dropna(how='all'))

# 不想删除，可以填充
print("\n填充缺失值")
print(df.fillna(0))

print("\n均值填充缺失值")
print(df.fillna(df.mean()))  # mean 平均

print("\n均值填充最大值")
print(df.fillna(df.max()))

print("\n均值填充最小值")
print(df.fillna(df.min()))
