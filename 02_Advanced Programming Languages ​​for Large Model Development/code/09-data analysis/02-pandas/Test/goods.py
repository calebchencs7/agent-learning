import pandas as pd

"""
背景：
某商店导出了一批订单数据。店长想知道每个商品分类的销售总额，并找出销售额最高的分类，方便后续制定进货策略。
请使用 Pandas 完成以下需求：
1.创建 DataFrame。(2分)
2.新增一列 amount，表示 price * count。(2分)
3.按 category 分组统计销售总额。(2分)
4.按销售总额从高到低排序。(2分)
5.输出统计结果。(2分)

"""

orders = [
    {"category": "图书", "price": 30, "count": 4},
    {"category": "文具", "price": 5, "count": 20},
    {"category": "图书", "price": 45, "count": 2},
    {"category": "数码", "price": 300, "count": 1},
    {"category": "文具", "price": 8, "count": 10},
]

df = pd.DataFrame(orders)

df["amount"] = df["price"] * df["count"]

grouped = df.groupby("category")["amount"].sum()

# 按销售总额从高到低排序
grouped = grouped.sort_values(ascending=False)

print(grouped)
