# 需求: 猜1-10数字,共1次机会,提示:大了,小了,对了
# 1.先有底数
import random

dishu = random.randint(1, 10)
# print(f'悄悄告诉你底数是:{dishu}')
# 2.用户猜
user_number = int(input('请您输入猜的整数(要求1-10):'))
# 3.判断并给提示
if user_number == dishu:
    print('猜对了')
else:
    if user_number > dishu:
        print('猜大了,重新猜')
    else:
        print('猜小了,重新猜')
