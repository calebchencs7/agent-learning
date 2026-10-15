"""
读取products.csv 转为pandas的DataFrame，删除缺失值的行
剩余内容，按自营非自营分组，统计平均价格
"""

import pandas as pd

df = pd.read_csv('../data/products.csv', sep=',')
print(df)
print("=" * 20)
# 删除缺失行
# 需要重新赋值给原有df
# df = df.dropna()          # df本身不变，返回新的DataFrame

# 不想重新赋值,可以用inplace=True参数，直接修改df本身
df.dropna(inplace=True)

print(df)
print("=" * 20)

result_df = df.groupby('is_self')['price'].mean()
print(result_df)
