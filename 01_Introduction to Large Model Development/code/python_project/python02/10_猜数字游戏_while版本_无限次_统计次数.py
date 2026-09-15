# 需求: 猜1-10数字,直到猜对为止,然后统计你猜了多少次猜对的!!!
# 1.先有底数
import random

rand_number = random.randint(1, 10)
# 5.1 循环外设置一个初始变量充当计数器
count = 0
# 4.循环
while True:
    # 2.获取到用户猜的数
    user_number = int(input("请您输入猜的数,范围1-10:"))
    # 5.2 循环内累加用户每猜完1次计数器加1
    count += 1

    # 3.判断
    if 1 <= user_number <= 10:
        if user_number == rand_number:
            print("猜对了")
            # 跳出循环
            break
        elif user_number > rand_number:
            print("猜大了")
        else:
            print("猜小了")
    else:
        print("您输入的数字无效,重新猜")

# 5.3 循环外打印最终结果
print(f"恭喜您,猜了{count}次猜对了")
