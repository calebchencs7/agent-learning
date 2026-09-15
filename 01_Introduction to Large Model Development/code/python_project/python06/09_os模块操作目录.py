import os

"""
os.rename(目标文件名称，新文件名称)                         创建指定名称的文件
os.remove(要删除的文件名称)                                删除指定名称的文件
os.mkdir(新文件夹名称)                                    创建一个指定名称的文件夹
os.getcwd()                                             获取当前目录名称
os.chdir(切换后目录名称)                                  切换目录
os.listdir(目标目录)                                     获取指定目录下的文件信息，返回列表 
os.rmdir(目标目录)                                       删除一个指定名称的空文件夹
"""

# 创建目录
# os.mkdir('./python06/aa')
# os.mkdir('./python06/demo1')

# 创建多层目录
# os.makedirs('./python06/aa/bb/cc')

# 删除单层空目录
# os.rmdir('./python06/demo1')

# 删除多层空目录
# os.removedirs("./python06/aa/bb/cc")

# 获取当前工作目录
# print("Current work directory:", os.getcwd())
# print(os.listdir(), end='\n')

# 切换默认工作目录
# os.chdir("./python05")
# print("Current work directory:", os.getcwd())

# 查看hm.jpg是否存在
# exists = os.path.exists("./python06/hm.jpg")
# print(exists)

# 查看当前目录下有哪些文件
# result = os.listdir("./python06")
# for i in result:
#     # 判断目录里面是不是文件
#     if os.path.isfile("./python06/" + i):
#         print(f"{i}是文件")
#     else:
#         print(f"{i}不是文件")
