from student_ms import StudentMS

# 创建管理系统类对象
sms = StudentMS()

while True:
    user_input = sms.print_info()

    if user_input == '0':
        print('用户输入0，退出程序')
        break

    if user_input == '1':
        sms.add()
        print()
    elif user_input == '2':
        sms.modify()
        print()
    elif user_input == '3':
        sms.delete()
        print()
    elif user_input == '4':
        sms.query()
        print()
    elif user_input == '5':
        sms.show()
        print()
    elif user_input == '6':
        sms.save()
        print()
    else:
        print("胡乱输入什么，重来。")
        print()

print("欢迎下次光临，再见")
