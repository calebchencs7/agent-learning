# 传统方式必须手动关闭文件对象,with open方式会自动关闭文件对象
import os

filename = "./python06/hello.txt"

# # 1. 写入初始数据
# with open(filename, 'w', encoding="utf-8") as f:
#     f.write("hello world")

# # 拆分路径：path_dir 为 "./python06"，base_name 为 "hello.txt"
# path_dir, base_name = os.path.split(filename)

# # 拼接出带有前缀的新路径：./python06/[备份]hello.txt
# backup_filename = os.path.join(path_dir, f"[备份]{base_name}")

# # 2. 读取并备份文件
# with open(filename, 'r', encoding="utf-8") as f_in:
#     with open(backup_filename, 'w', encoding="utf-8") as f_out:
#         data = f_in.read()
#         f_out.write(data)
#         print(f"备份成功，生成文件：{backup_filename}")


import os

filename = "./python06/hello.txt"

# 1. 写入初始数据
with open(filename, 'w', encoding="utf-8") as f:
    f.write("hello world")

# 拆分路径：path_dir 为 "./python06"，base_name 为 "hello.txt"
path_dir, base_name = os.path.split(filename)

# 拼接出带有前缀的新路径：./python06/[备份]hello.txt
backup_filename = os.path.join(path_dir, f"[备份]{base_name}")

# 2. 读取并备份文件
with open(filename, 'r', encoding="utf-8") as f_in, open(
        backup_filename, 'w', encoding="utf-8"
) as f_out:
    data = f_in.read()
    f_out.write(data)
    print(f"备份成功，生成文件：{backup_filename}")
