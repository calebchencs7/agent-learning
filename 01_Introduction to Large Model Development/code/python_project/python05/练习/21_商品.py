"""
假设我们有一个存储商品价格的列表 prices，每个元素代表一个商品的价格。现在需要完成以下任务：
将价格列表按升序排序。
将价格列表反转，以得到降序排序的列表。
找到最高价格和最低价格。
计算所有商品的平均价格。
"""

prices = [19.99, 5.49, 3.99, 12.99, 7.99]
prices.sort()
print("升序排序:", prices)
prices.reverse()
print("降序排序:", prices)
print("最高价格:", max(prices))
print("最低价格:", min(prices))
print("平均价格:", sum(prices) / len(prices))
