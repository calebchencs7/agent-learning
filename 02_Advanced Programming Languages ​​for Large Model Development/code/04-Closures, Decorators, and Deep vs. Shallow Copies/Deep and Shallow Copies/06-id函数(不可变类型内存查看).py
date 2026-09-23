# 不可变类型发生修改，是修改了变量的指向，而不是修改了内存中的值
# 不可变类型：数据一旦存入内存，不可以修改，只能删除
a = 10
b = 10

# id，查看变量记录的内存地址
# 不可变类型值相同，指向同一块内存地址
print(id(a))  # 4319570648
print(id(b))  # 4319570648

s1 = "itheima"
s2 = "itheima"
print(id(s1))  # 4298732624
print(id(s2))  # 4298732624

print("-" * 20)

num1 = 10
print(id(num1))  # 4319570648
num1 = 20
print(id(num1))  # 4319570968
print("-" * 20)

a = 10
b = a
print(id(a))  # 4319570648
print(id(b))  # 4319570648
b = 20  # b的修改不影响a
print(a)  # 10
print(b)  # 20
print(id(a))  # 4319570648
print(id(b))  # 4319570968
