# 接口：设计规范，要求实现（生产实体）接口要对着规范做
# 接口：图纸，  实现就是施工，施工要对着图纸来

from abc import ABC, abstractmethod


# 让抽象类继承ABC
# 抽象类，指导类设计的图纸
class ABCFileService(ABC):  # ABC -> abstract 抽象   也叫接口
    """
    @abstractmethod 是 Python 的抽象方法装饰器，表示该方法只是定义规范，要求具体子类必须实现。
    """

    @abstractmethod
    def read_oneline(self) -> str:
        """
        ...
        :return:
        """
        pass

    @abstractmethod
    def write_oneline(self, context: str) -> bool:
        pass

    @abstractmethod
    def print_all(self) -> None:
        pass

    @abstractmethod
    def read_all(self) -> str:
        pass


class TextFileService(ABCFileService):
    def __init__(self, file_path):
        self.fr = open(file_path, "r", encoding="UTF-8")
        self.fw = open(file_path, "a", encoding="UTF-8")

    def read_oneline(self) -> str:
        return self.fr.readline()

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


tfs = TextFileService("data.txt")
tfs.write_oneline("abcde")
tfs.write_oneline("啦啦啦啦啦")
print(tfs.read_oneline())
