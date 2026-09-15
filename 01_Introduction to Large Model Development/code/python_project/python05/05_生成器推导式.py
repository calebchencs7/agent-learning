# 注意: 生成器推导式用的符号是小括号
# 很多同学会认为是元组推导式,元组没有推导式

# 快速生成1-10的生成器generator对象
g1 = (i for i in range(1, 10))
print(g1)
print(type(g1))

# 注意: 虽然不能直接生成元组,但是可以使用tuple()转换
t1 = tuple(i for i in range(1, 10))
print(t1)
print(type(t1))

# 也能转换为其他类型
l1 = list(i for i in range(1, 10))
print(l1)
print(type(l1))

s1 = set(i for i in range(1, 10))
print(s1)
print(type(s1))
