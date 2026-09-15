# 需求: 模拟先注册用户,然后用户登录,判断登录成功/失败
# 1.假设用户注册信息: 用户名:admin,密码:a123
name = 'admin'
pwd = 'a123'
# 2.用户键盘录入登录信息
user_name = input('请您输入用户名:')
user_pwd = input('请您输入密码:')
# 3.比较并给提示
if user_name == name and user_pwd == pwd:
    print('登录成功!')
else:
    print('用户名或者密码错误!')
