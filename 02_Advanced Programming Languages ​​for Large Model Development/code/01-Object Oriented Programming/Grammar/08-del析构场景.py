class FileWriteService:

    def __init__(self, file_path, encoding="UTF-8"):
        self.file = open(file_path, "w", encoding=encoding)

    def write_line(self, content):
        self.file.write(content)
        self.file.write("\n")

    def __del__(self):
        print("即将被销毁，保存资料到硬盘")
        self.file.flush()  # 将缓冲区中尚未写入磁盘的数据立即写入文件
        # 把文件的关闭写到对象析构函数内，就可以自动关闭文件了
        self.file.close()  # 关闭文件，同时也会自动执行一次 flush


fws = FileWriteService("data.txt")
fws.write_line("大家好")
fws.write_line("你好")
fws.write_line("哈基米好")
