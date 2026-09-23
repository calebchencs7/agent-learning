# 深浅拷贝主要用于 可变类型
# 可变：```列表```、集合、字典
# 不可变：```字符串```、```元组```
# 等号是直接引用赋值，lst1和lst2指向同一个列表对象，修改其中一个会影响另一个
lst1 = [1, 2, 3]
lst2 = lst1

print(lst1)
print(lst2)

lst2.append(4)

print(lst1)
print(lst2)

lst1.pop(0)
print(lst1)
print(lst2)
