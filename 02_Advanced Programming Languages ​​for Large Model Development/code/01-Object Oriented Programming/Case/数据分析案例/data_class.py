# 用类对象存放数据
class DataClass:

    def __init__(self, date: str, order_id: str, sale_amount: float, province: str):
        self.date = date
        self.order_id = order_id
        self.sale_amount = sale_amount
        self.province = province

    # 输出类对象魔法方法
    def __str__(self):
        return f"{self.date},{self.order_id},{self.sale_amount},{self.province}"

    # 如果对象在容器内，要输出，需要用__repr__这个魔法方法
    def __repr__(self) -> str:
        return f"{self.date},{self.order_id},{self.sale_amount},{self.province}"


# # 用类对象，存放数据
# class DataClass:
#     def __init__(self, date, order_id, sale_amount, province):
#         self.date = date
#         self.order_id = order_id
#         self.sale_amount = sale_amount
#         self.province = province

#     def __str__(self):
#         return f"{self.date},{self.order_id},{self.sale_amount},{self.province}"

#     # 如果对象在容器内，要输出，需要用__repr__
#     def __repr__(self):
#         return f"{self.date},{self.order_id},{self.sale_amount},{self.province}"

# # int float 单值
# # list[... . . .. . ]
# # tuple(. . . . . .)
# # set{. . . . . . }
# # str ". . . . . . "
# # dict {kv kv kv kv}
# # 属性（变量）
# # 行为（函数方法）
# # dc = DataClass()
# # dc.date = ?
# # dc.orderid=?
# # dc.sale_amount = ?
# # dc.province = ?

# # l = [1, 2, 3]
# # <class list>  < class DataClass>
