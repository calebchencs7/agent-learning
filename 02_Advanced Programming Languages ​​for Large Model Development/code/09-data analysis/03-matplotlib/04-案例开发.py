import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = (
    False  # 让坐标轴上的负数使用普通减号 -，代替默认的 Unicode 负号 −
)

# 1. 读取数据
df = pd.read_csv("../data/1960-2019全球GDP数据.csv", sep=",", encoding="GBK")

# 2. 删除空值
df.dropna(inplace=True)

# 3. 提取中美日三个国家各自的数据集
# df[df[列] == 值]
df_cn = df[df['country'] == '中国'].copy()  # copy浅拷贝
df_jp = df[df['country'] == '日本'].copy()  # copy浅拷贝
df_us = df[df['country'] == '美国'].copy()  # copy浅拷贝
df_uk = df[df['country'] == '英国'].copy()  # copy浅拷贝

# 4. 图表生成
# x 轴
df_cn_x = df_cn['year']
df_jp_x = df_jp['year']
df_us_x = df_us['year']
df_uk_x = df_uk['year']
# y 轴
df_cn_y = df_cn['GDP']
df_jp_y = df_jp['GDP']
df_us_y = df_us['GDP']
df_uk_y = df_uk['GDP']

# 画布
plt.figure(figsize=(10, 6))
# 填充x和y
plt.plot(df_cn_x, df_cn_y, color='red', label='中国')  # label这根线的名字
plt.plot(df_jp_x, df_jp_y, color='blue', label='日本')
plt.plot(df_us_x, df_us_y, color='green', label='美国')
plt.plot(df_uk_x, df_uk_y, color='yellow', label='英国')
# 标题
plt.title("中美日英GDP")
# 显示图例
plt.legend()  # 显示各个线的名字
# 网格
plt.grid()

# 显示
plt.show()
