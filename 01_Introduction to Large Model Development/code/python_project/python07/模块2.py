# 功能函数
def show():
    print('模块2中的show执行了')


def get_sum(a, b):
    print('模块2中get_sum执行了')
    return a + b


if __name__ == '__main__':
    # 只有在当前文件运行,__name__才等于__main__
    show()
