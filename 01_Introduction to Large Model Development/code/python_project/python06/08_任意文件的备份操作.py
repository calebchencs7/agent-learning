# 需求: 编写一个程序,完成任意文件的备份操作
# 获取用户要备份文件
file_name = input('请您输入要备份的文件(默认当前路径):')
# TODO 先判断file_name是否存在,如果不存在给提醒,存在再去备份
# try 块：存放可能抛出异常的代码（比如打开文件）。
try:
    # 打开文件
    f_in = open("./python06/" + file_name, mode='rb')
    f_out = open(f'./python06/[备份]{file_name}', mode='wb')
# except 块：当 try 块中的代码发生错误/抛出异常时执行。
except Exception as e:
    print(f"报错了啊,{e}")
# 当 try 块中的代码完全没有报错、顺利执行完毕时执行else
else:
    # 文件备份(先读再写)
    data = f_in.read()
    f_out.write(data)
    print(f'{file_name}备份成功')
finally:
    # 文件关闭
    f_out.close()
    f_in.close()
