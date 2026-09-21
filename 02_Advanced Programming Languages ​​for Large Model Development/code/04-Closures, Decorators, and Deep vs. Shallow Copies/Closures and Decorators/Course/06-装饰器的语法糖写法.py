# 1. 通过闭包模拟实现对一个函数的增强
# 2. 被增强函数随意，内容随意
# 3. 增强的效果就是：增强后函数执行先输出一句话：我干活了


def buff(fn):

    def inner():
        print("我干活了")
        fn()  # fn指代原有未被增强的函数本身

    return inner


@buff
def say_hi():
    print("我好帅哦")


# say_hi = buff(say_hi)

say_hi()
