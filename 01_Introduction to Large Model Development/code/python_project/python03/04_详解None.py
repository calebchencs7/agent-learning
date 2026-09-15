# None: 代表空的,没有任何意义的意思
# 注意: 如果你自定义函数的时候,没有写return 返回值,解释器会自动在函数的最后一行补充return None
# 1.先定义函数
def show():
    print("show函数执行了~")
    # 默认底层会在程序最后一行:自动补充return None


# 2.再调用函数
# 如果自定义函数没有显式的写出return 返回值,那调用的时候就不要用变量接收
a = show()  # show函数执行了~
print(a)  # None
