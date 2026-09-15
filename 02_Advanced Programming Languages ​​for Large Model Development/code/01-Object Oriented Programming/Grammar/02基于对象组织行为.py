
class Student:
    name = None
    age = None
    gender = None

    # class中还可以写函数
    def say_hi(self):
        print(f"大家好，我叫{self.name}，今年{self.age}岁，我是{self.gender}生")

# 产生对象
stu1 = Student()
stu2 = Student()

# 给对象记录数据
stu1.name = "周杰轮"
stu1.age = 18
stu1.gender = "男"

stu2.name = "王力宏"
stu2.age = 11
stu2.gender = "女"

#
stu1.say_hi()
stu2.say_hi()
