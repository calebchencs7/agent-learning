import pandas as pd

df = pd.read_csv("../data/分组聚合数据.csv", sep=",")

print(df)
# 分组统计  group by + 聚合
# group by 产品 sum(销售额)
print("\n按产品分组统计销售额的和")
# df.groupby(列)[列].sum|min|max|mean|count()
print(df.groupby('产品')['销售额'].sum())


print("\n按产品分组统计销售额的最小")
print(df.groupby('产品')['销售额'].min())


# 多列分组，多聚合
# select sum(销售额), avg(销售额) from df group by 产品, 地区;
print("\n按产品和地区分组统计销售额的和以及平均")
# df.groupby([列,列])[列].agg(['sum', 'mean', 'max', ...])
print(df.groupby(['产品', '地区'])['销售额'].agg(['sum', 'mean']))


print("\n数据透视表")
# 产品分组  sum销售额
pivot_df = df.pivot_table(index='产品', values='销售额', aggfunc='sum')
print(pivot_df)
