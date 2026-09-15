class Student:
    """
    学生类
    """

    def __init__(self, name: str, gender: str, tel: str, age: int, info: str) -> None:
        """
        初始化学生对象
        :param name: 学生姓名
        :param gender: 学生性别
        :param tel: 学生电话
        :param age: 学生年龄
        :param info: 学生其它信息
        """
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.info = info

    def __str__(self):
        """
        将学生对象，转换为字符串，写入文件
        :return: 转换后的字符串
        """
        # return ",".join([self.name, self.gender, self.tel, str(self.age), self.info])
        return f"{self.name},{self.gender},{self.tel},{self.age},{self.info}"

    @staticmethod
    def generate(stu_str: str) -> "Student":
        """
        通过字符串生成学生对象
        :param stu_str: 学生信息字符串
        :return: 学生对象
        """
        arr = stu_str.split(",")
        return Student(arr[0], arr[1], arr[2], int(arr[3]), arr[4])
