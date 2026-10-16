"""
背景：
某文具店想统计不同商品分类的销售总额，并找出销售表现较好的分类。为了让结果更直观，还需要将各分类销售总额绘制成柱状图。
题目：
现有商品销售数据如下：

orders = [
    {"category": "图书", "amount": 120},
    {"category": "文具", "amount": 80},
    {"category": "图书", "amount": 200},
    {"category": "数码", "amount": 500},
    {"category": "文具", "amount": 150}
]
请完成以下要求：
1.使用 Pandas 将数据转换为 DataFrame。(2分)
2.按 category 分组，统计每个分类的销售总额。(2分)
3.输出销售总额大于 200 的分类。(2分)
4.使用 Matplotlib 绘制各分类销售总额柱状图。(3分)
"""

import pandas as pd
import matplotlib.pyplot as plt

# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = (
    False  # 让坐标轴上的负数使用普通减号 -，代替默认的 Unicode 负号 −
)


orders = [
    {"category": "图书", "amount": 120},
    {"category": "文具", "amount": 80},
    {"category": "图书", "amount": 200},
    {"category": "数码", "amount": 500},
    {"category": "文具", "amount": 150},
]


pd_orders = pd.DataFrame(orders)


# 按 category 分组，统计每个分类的销售总额
category_sales = pd_orders.groupby("category")["amount"].sum()

print("各分类销售总额:")
print(category_sales)

# 输出销售总额大于 200 的分类
high_sales_categories = category_sales[category_sales > 200]
print("\n销售总额大于 200 的分类:")
print(high_sales_categories)

# 绘制各分类销售总额柱状图
plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values, color='skyblue')
plt.title("各分类销售总额柱状图")
plt.xlabel("分类")
plt.ylabel("销售总额")
plt.grid()
plt.show()
