# 1.先定义函数
def show1(name, age, weight):
    print(f"姓名:{name},年龄:{age},体重:{weight}kg")


# 默认参数: 在定义函数的时候可以提前给参数设置默认值
def show2(name='张三', age=18, weight=66.66):
    print(f"姓名:{name},年龄:{age},体重:{weight}kg")


if __name__ == '__main__':
    # 2.再调用函数
    # 位置传参:实参和形参个数以及位置都必须一致!!!
    show1('张三', 18, 66.66)

    # 关键字传参:实参和形参个数必须一致,但是位置可以不一致
    show1(age=18, name='张三', weight=77.77)

    # 位置传参和关键字传参如果一起使用,位置传参必须放到前面
    show1('张三', age=18, weight=88.88)

    print()

    # todo 有了默认参数后,实参和形参的个数不是必须一致的
    show2()
    show2('李四')
    show2(age=28)
    show2('王五', weight=99.99)
    show2('王五', weight=99.99, age=38)
