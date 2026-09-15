class Student:

    def __str__(self):  # 必须叫做 __str__
        """当类对象被转为字符串的时候，应当返回什么结果
        - 默认print(对象)的时候打印的是对象的内存地址，
        - 但是可以用__str__(self)方法去控制这种默认类对象被转换为字符串的时候的行为
        - 即这个方法，在类对象被转换为字符串的时候，自动被调用
        """
        return f"我叫{self.name}，今年{self.age}岁"

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("王大锤", 11)
print(stu)

s = str(stu)
print(s)
