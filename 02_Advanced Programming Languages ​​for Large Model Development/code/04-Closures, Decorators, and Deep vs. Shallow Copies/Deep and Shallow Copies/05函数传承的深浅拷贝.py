def process(lst):
    lst.append(100)


lst1 = [1, 2, 3]
process(lst1)  # 等于 = 赋值
print(lst1)

process(lst1.copy())
print(lst1)
