import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = (
    False  # 让坐标轴上的负数使用普通减号 -，代替默认的 Unicode 负号 −
)


df = pd.read_csv('1960-2019全球GDP数据.csv', sep=',', encoding='gbk')

# 干掉空值
# inplace=True 表示原地更改，即修改自己，不会返回新的DataFrame
df.dropna(inplace=True)

# 过滤
# .copy()就是复制一份数据返回，避免对老的DataFrame产生影响
df_cn = df[df['country'] == '中国'].copy()
df_jp = df[df['country'] == '日本'].copy()
df_us = df[df['country'] == '美国'].copy()

# 将年份设置为索引值，x轴数据一般被拿来做索引
df_cn.set_index('year', inplace=True)
df_jp.set_index('year', inplace=True)
df_us.set_index('year', inplace=True)

# 为了避免图例的冲突，将每份数据的GDP列名改为各自国家
df_cn.rename(columns={"GDP": "中国"}, inplace=True)
df_jp.rename(columns={"GDP": "日本"}, inplace=True)
df_us.rename(columns={"GDP": "美国"}, inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(df_cn.index, df_cn["中国"], color="red", label="中国")  # label给这个线起名
plt.plot(df_jp.index, df_jp["日本"], color="green", label="日本")
plt.plot(df_us.index, df_us["美国"], color="blue", label="美国")
plt.title("中美日GDP")
plt.legend()  # 显示图例
plt.grid()

plt.show()
