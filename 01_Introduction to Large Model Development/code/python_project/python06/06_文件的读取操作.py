# 需求: 已知本地test.txt文件,要求把其中所有内容读出,展示到控制台
# 1.打开文件
f = open('./python06/hm.jpg', mode='rb')
# 2.读取文件
# read()一个字符一个字符读,直到读完所有(读取文件、图片、视频均可用)
data = f.read()
print(data)

# readline() 一次读取一行（读文件用）
# data = f.readline()
# print(data)

# readlines() 一行行读，直到读取所有（读文件用）
# data = f.readlines()
# print(data)


# 关闭文件
f.close()
