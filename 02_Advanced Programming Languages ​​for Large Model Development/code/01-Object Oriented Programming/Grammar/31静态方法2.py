class TextFileService:
    def __init__(self, file_path):
        self.fr = open(file_path, "r", encoding="UTF-8")
        self.fw = open(file_path, "a", encoding="UTF-8")

    def write_oneline(self, context: str) -> bool:
        try:
            self.fw.write(context)
            self.fw.write("\n")
            return True
        except Exception:
            return False

    def print_all(self) -> None:
        self.fr.seek(0)
        print(self.fr.read())

    def read_all(self) -> str:
        self.fr.seek(0)
        return self.fr.read()

    @staticmethod
    def print_info():
        print("======欢迎使用黑马程序员文件服务======")
        print("======您可以使用如下方法：======")
        print("1. write_oneline,写入一行数据")
        print("2. print_all,打印全部信息")
        print("3. read_all,读取全部信息")
        print("======祝您用的爽歪歪======")
        print("BBBBBBBBBBBBBBBBBBBBBBBB")


def print_info():
    print("======欢迎使用黑马程序员文件服务======")
    print("======您可以使用如下方法：======")
    print("1. write_oneline,写入一行数据")
    print("2. print_all,打印全部信息")
    print("3. read_all,读取全部信息")
    print("======祝您用的爽歪歪======")
    print("AAAAAAAAAAAAAAAAAAAA")


# print_info()
TextFileService.print_info()
