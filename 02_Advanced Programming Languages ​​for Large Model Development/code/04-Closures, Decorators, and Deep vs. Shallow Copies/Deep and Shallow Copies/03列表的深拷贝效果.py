# 如果列表中有嵌套列表，浅拷贝只复制外层，内层仍然共用
# 所以在这种情况下，使用深拷贝可以创建一个完全独立的副本，包括嵌套的列表。
import copy

lst1 = [1, 2, ["a", "b", "c"]]
lst2 = copy.deepcopy(lst1)

print(lst1)
print(lst2)


lst2.append(3)
print(lst1)
print(lst2)

lst2[2].append("d")
print(lst1)
print(lst2)
