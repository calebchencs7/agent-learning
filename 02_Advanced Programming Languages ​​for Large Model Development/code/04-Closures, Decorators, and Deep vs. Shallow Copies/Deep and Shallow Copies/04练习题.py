# 创建lst1，内含3个数字
# 通过浅拷贝，复制给lst2，让2者分离
#
# 创建lst3，内含2个数字和一个嵌套list
# 通过深拷贝，复制给lst4，分离2者
import copy

lst1 = [1, 2, 3]
# 浅拷贝写法1
# lst2 = copy.copy(lst1)
# 浅拷贝写法2
lst2 = lst1.copy()
lst2.append(4)
print(lst1)
print(lst2)

print("-"*20)

lst3 = [1, 2, [3, 4, 5]]
lst4 = copy.deepcopy(lst3)

lst4[2].append(6)
print(lst3)
print(lst4)