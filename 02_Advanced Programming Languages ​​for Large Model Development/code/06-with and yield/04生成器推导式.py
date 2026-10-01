lst1 = [i for i in range(1, 6)]
print(lst1)  # lst1内存放全部10000个元素

num_generator = (i for i in range(1, 6))  # lst2 c生成器对象
print(num_generator)
# lst2 生成器，记录生成数据的规则，即记下来了```i for i in range(1, 10001)```
print(next(num_generator))  # 使用next(生成器)，按生成规则，临时产生一条数据给你
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
# print(next(num_generator))  # 规则耗尽就无法得到下一个了

# 如果要找到生成器结束的临界点，手动捕获StopIteration异常即可
while True:
    try:
        print(next(num_generator))
    except StopIteration:
        print("生成器用完了")
        break


# 生成器也支持for循环
for num in num_generator:
    print(num, end=" ")
