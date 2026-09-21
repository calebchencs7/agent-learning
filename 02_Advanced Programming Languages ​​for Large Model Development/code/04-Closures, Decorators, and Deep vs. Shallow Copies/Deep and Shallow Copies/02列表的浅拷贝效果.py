# 浅拷贝会创建一个新的对象，但如果列表中还有嵌套列表，浅拷贝只复制外层，内层仍然共用：


lst1 = [1, 2, 3]
lst2 = lst1.copy()

print(lst1)
print(lst2)

lst2.append(4)

print(lst1)
print(lst2)
