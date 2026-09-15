# 需求: 猜1-10数字,共3次机会,提示:大了,小了,对了
# 注意: 循环终止条件要么次数够了,要么猜对了
import random

dishu = random.randint(1, 10)  # 底数
print(dishu)
# 1.定义循环初始变量,赋初始值
i = 1
# 2.while条件判断
while i <= 3:
    # 3.循环体
    user_number = int(input('请您输入猜的整数(要求1-10):'))  # 用户猜的数
    if user_number == dishu:  # 判断
        print('猜对了')
        # 结束循环,跳出循环
        break
    else:
        if user_number > dishu:
            print('猜大了,重新猜')
        else:
            print('猜小了,重新猜')
    # 4.条件控制
    i += 1

print('其他内容...')
