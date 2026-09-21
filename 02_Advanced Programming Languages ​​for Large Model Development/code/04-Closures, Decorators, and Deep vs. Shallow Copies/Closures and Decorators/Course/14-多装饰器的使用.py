def login_check(fn):

    def inner():
        print("登录验证通过")
        fn()  # codecheck(fn)

        return "B"

    return inner


def code_check(fn):

    def inner():
        print("验证码验证通过")
        fn()
        return "A"

    return inner


# 按照装饰器的顺序，先执行login_check，再执行code_check
@login_check
@code_check
def comment():
    print("这家餐馆真好吃")


# comment = login_check(code_check(comment))
# comment ==> login_check的inner  返回值是login_check inner的返回值
comment()
