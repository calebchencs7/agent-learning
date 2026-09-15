# 1. 设计一个Student class  包含共享的类属性 school_name = "黑马"
class Student:
    school_name = "黑马"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 在class中设计 init 接收name和age2个参数，用于设计成员属性
# 创建2个学生，有不同的名字和age
stu1 = Student("王大锤", 11)
stu2 = Student("张翠花", 3)
# 打印学生的名字、age、和学校名字
print(stu1.name, stu1.age, stu1.school_name)
print(stu2.name, stu2.age, stu2.school_name)
#
# 5. 修改学校名字
Student.school_name = "白马"
# 6. 再次打印2个学生的名字 age 和学校名字
print(stu1.name, stu1.age, stu1.school_name)
print(stu2.name, stu2.age, stu2.school_name)
