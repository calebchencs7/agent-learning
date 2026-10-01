# 得到一个生成器对象（推导式得到）
# 生成器对象的规则是，生成从1到100（包含）的偶数
#
# for循环生成器，输出每一个数字

num_gen = (i for i in range(1, 101) if i % 2 == 0)

# for loop generator, output each number
for num in num_gen:
    print(num)
