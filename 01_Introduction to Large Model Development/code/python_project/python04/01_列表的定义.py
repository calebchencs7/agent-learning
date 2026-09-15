# 1.定义空列表
l1 = []
l2 = list()
print(l1, l2)
print(type(l1), type(l2))

# 2.定义非空列表
l3 = [10, 20, 20, '张三', '李四', True, True, 3.14]
print(l3)

# 虽然列表可以存储任意类型,但是建议同类型单独存储
l4 = ['张三']
print(type(l4))
l5 = [18, 28]

# 列表经常会嵌套使用
l6 = [l4, l5]
print(l6)
