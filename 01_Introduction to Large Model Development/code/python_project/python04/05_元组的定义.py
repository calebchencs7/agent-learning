# 定义空元组
t1 = ()
t2 = tuple()
print(t1, t2)
print(type(t1), type(t2))

# 定义非空元组
t3 = (10, 3.14, '张三', True)
print(t3, type(t3))

# 注意: 如果元组中只存储1个元素,必须加逗号
t4 = (10,)
print(t4, type(t4))
# 注意: 元组也可以支持嵌套
t5 = (t3, t4)
print(t5, type(t5))
