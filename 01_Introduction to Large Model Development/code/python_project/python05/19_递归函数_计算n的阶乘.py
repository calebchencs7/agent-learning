# 1.明确函数是干什么的
def get_factorial(n):
    # 2.明确出口
    if n == 1:
        return 1
    # 3.找规律
    return n * get_factorial(n - 1)
    #   5*4*3*2*get_factorial(1)


print(get_factorial(5))
