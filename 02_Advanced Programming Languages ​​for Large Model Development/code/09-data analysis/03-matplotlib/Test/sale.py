import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

"""
背景：
某门店每个月都会统计不同商品分类的销售额。店长不仅想看到整体销售额的变化趋势，还想知道哪个分类贡献更高，因此需要把数据整理后画成图表，方便做经营分析。
题目：

请使用 Pandas 和 Matplotlib 完成以下需求：
1.创建 DataFrame。(2分)
2.统计每个月的总销售额，并绘制折线图。(2分)
3.统计每个商品分类的总销售额，并绘制柱状图。(2分)
4.图表需要设置标题、横轴名称、纵轴名称。(2分)
5.可以使用 plt.show() 展示图表。(2分)
【提交代码和运行截图】

"""

matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = (
    False  # 让坐标轴上的负数使用普通减号 -，代替默认的 Unicode 负号 −
)

sales = [
    {"month": "1月", "category": "图书", "amount": 1200},
    {"month": "1月", "category": "文具", "amount": 800},
    {"month": "2月", "category": "图书", "amount": 1500},
    {"month": "2月", "category": "文具", "amount": 950},
    {"month": "3月", "category": "图书", "amount": 1800},
    {"month": "3月", "category": "文具", "amount": 1100},
]


df = pd.DataFrame(sales)
sales_by_month = df.groupby("month")["amount"].sum()
print(sales_by_month)
sales_by_category = df.groupby("category")["amount"].sum()
print(sales_by_category)


# 绘制每个月的总销售额折线图
plt.figure(figsize=(10, 5))
plt.plot(sales_by_month.index, sales_by_month.values, marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# 绘制每个商品分类的总销售额柱状图
plt.figure(figsize=(10, 5))
plt.bar(sales_by_category.index, sales_by_category.values)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()
