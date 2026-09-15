# 已知a=10,b=20,如何快速交换值
a = 10
b = 20
print(a, b)

# 原始方式
c = a
a = b
b = c
print(a, b)

# 打包拆包
a, b = b, a
print(a, b)
