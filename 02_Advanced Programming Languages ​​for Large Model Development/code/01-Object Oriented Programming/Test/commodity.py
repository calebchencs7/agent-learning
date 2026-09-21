"""
商品价格管理
商品价格管理：定义商品类
背景：
商店系统中需要管理商品价格。为了后续扩展库存、折扣活动等功能，先用类保存商品名称和单价，并提供方法计算打折后的价格。
题目：
定义一个 Product 类，要求：
1.构造方法接收 name 和 price 两个参数，并保存为实例属性。 (2分)
2.实现 get_discount_price(rate) 方法，返回打折后的价格，计算公式为 price * rate。 (3分)
3.实现 str() 方法，返回格式为：商品：图书，单价：50。 (3分)
4.在主程序中创建 Product("图书", 50) 对象，打印对象，并打印 8 折后的价格。 (2分)
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discount_price(self, rate):
        return self.price * rate

    def __str__(self):
        return f"商品：{self.name}，单价：{self.price}"


if __name__ == "__main__":
    product = Product("图书", 50)
    print(product)
    discount_price = product.get_discount_price(0.8)
    print(f"8折后的价格：{discount_price}")
