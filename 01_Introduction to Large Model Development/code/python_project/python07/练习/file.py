import os

filepath = "./python07/练习/python.txt"
if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = file.read()
        print(data)
else:
    print(f"错误：未在当前工程路径下找到文件 {file_path}")
