"""
假设你正在开发一个在线商店的购物车功能，需要编写 Python 代码来处理购物车内的商品。请完成以下要求：
已知有一个购物车商品列表 cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]，
其中每个元组表示一种商品及其数量。请编写代码，实现以下功能：
创建一个新列表 cart_items，其中仅包含购物车中的商品名称（即去除商品数量信息）。
创建一个新列表 expensive_items，其中仅包含购物车商品数量>=3的商品名称。
将购物车中每个商品的数量加倍，并创建一个新的购物车列表 cart_doubled。
请编写上述要求的代码，并输出最终的列表 cart_items、expensive_items 和 cart_doubled。
"""

cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]
cart_items = [name for name, number in cart]
# cart_items = [item[0] for item in cart] 也可以
# cart_items = [name for name, _ in cart] 也可以
expensive_items = [name for name, number in cart if number >= 3]
cart_doubled = [(name, number * 2) for name, number in cart]

print(cart_items)
print(expensive_items)
print(cart_doubled)
