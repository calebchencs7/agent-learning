# 1. 参考如下写法
#  2. 提供一个文件读取类，类中有 __init__ 接收文件路径，打开文件，获得文件对象（成员属性）
# 3. 提供del析构方法，关闭文件
# 4. 提供一个readfile方法， 循环输出文件内容
#
#  注意，被读取的文件自行创建，内容随意


class FileReadService:
    """文件读取服务类"""

    def __init__(self, file_path, encoding="utf-8"):
        self.file = open(file_path, 'r', encoding=encoding)

    def __del__(self):
        self.file.close()

    def read_file(self):
        """读取并打印文件内容。"""
        data = self.file.read()
        print(data)


file = FileReadService("data.txt")
file.read_file()
