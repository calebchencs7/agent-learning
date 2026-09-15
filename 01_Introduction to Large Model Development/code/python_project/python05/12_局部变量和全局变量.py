# 1.先定义函数
def show1():
    # 局部变量
    a = 100
    print(a)  # 100
    print(b)  # 访问全局变量200


# 2.再调用函数
# 全局变量
if __name__ == '__main__':
    b = 200
    show1()
    print(b)  # 访问全局变量200
