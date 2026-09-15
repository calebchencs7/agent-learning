# 1.先定义函数
def show1():
    print('----show1函数开始----')
    print('show1此处省略1k行代码...')
    print('----show1函数结束----')


def show2():
    print('======show2函数开始=======')
    show1()
    print('======show2函数结束=======')


# 程序的入口是main
# 2.再调用函数
if __name__ == '__main__':
    print('main开始')
    show2()
    print('main结束')
