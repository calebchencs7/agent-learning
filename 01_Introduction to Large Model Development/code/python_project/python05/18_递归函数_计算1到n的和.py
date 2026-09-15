# 定义函数,计算1-n的累加和
# 1.明确函数要干什么
def get_sum(n):
    # 2.明确递归结束条件
    if n == 1:
        return 1
    # 3.找到规律
    return n + get_sum(n - 1)
    # 5 + 4 + 3 + 2+ get_sum(1)


num = int(input("请输入想从1累加到几？"))
# 调用函数
print(get_sum(num))
