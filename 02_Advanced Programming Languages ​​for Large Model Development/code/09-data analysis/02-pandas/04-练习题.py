import pandas as pd

data_list = [
    [1, '王大锤', 11],
    [2, '王小锤', 12],
    [3, '王屁锤', 12],
    [4, '王臭锤', 12],
]
df = pd.DataFrame(
    data_list, columns=['id', 'name', 'age'], index=['s1', 's2', 's3', 's4']
)
print(df)
print("=" * 20)
print(df.head(2))
print(df.tail(2))
print("=" * 20)
print(df.loc["s1":"s3"])
print("=" * 20)
print(df[['name', 'age']])
