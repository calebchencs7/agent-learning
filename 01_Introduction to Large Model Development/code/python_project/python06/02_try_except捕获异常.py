def demo01():
    print('--------程序第一行代码----------')
    try:
        a = int(input('请您输入一个数据作为除数:'))
        print(1 / a)
        # 如果上面报错，下面的代码就会被跳过不会被执行，程序会去进入到except里面
        my_list = [10, 20, 30]
        print(my_list[3])  # IndexError: list index out of range
    except (NameError, ZeroDivisionError, IndexError) as e:
        print(e)
    print('--------程序最后一行代码--------')
    print('其他程序代码...')


print('--------程序第一行代码----------')
try:
    # 把可能出错的代码放在try except块内
    a = int(input('请您输入一个数据作为除数:'))
    print(1 / a)
except Exception as e:
    print(f"除法报错了：{e}")

try:
    my_list = [10, 20, 30]
    print(my_list[3])
except Exception as e:
    print(f"列表报错了：{e}")
print('--------程序最后一行代码--------')

print('其他程序代码...')
