"""
1. 有嵌套
2. 内层引用外层变量（局部变量、形参）
3. 外层返回内层函数
4. 被修饰函数，在外层作为形参传入
5. 在内层函数内，对原有函数做功能增强（即提供不存在的能力）
"""

# 有一个发表评论的函数，为其增强功能：发表评论前，需要验证是否登录

LOGIN_STATUS = True


def check(fn):  # 被修饰函数，在外层作为形参传入

    def inner():  # 1. 有嵌套
        if LOGIN_STATUS:
            print("我已经登录可以评论了")  # 4. 内层中对原有函数做增强
            fn()  # fn就是被装饰的函数本身  # 2. 内层使用外层变量
        else:
            print("请先登录")

    return inner  # 3. 外层返回内层函数


def comment():
    print("这家烧烤真好吃！")


comment = check(comment)  # comment 鸠占鹊巢，本质上就是inner的逻辑

# 此时这个comment就不是原本的comment函数了，被inner顶包了
comment()  # 本质就是调用 inner()
