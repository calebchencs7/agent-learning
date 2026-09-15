# 设计一个Person类，内含name、age2个成员属性
#
# 内含 work()、sleep()、2个方法，内容随意
#
# 设计一个Student类继承Person类
# 给Student类提供属于他的 study()方法内容随意

class Person:
    def __init__(self):
        self.name = "王大锤"
        self.age = 11

    def work(self):
        print("牛会哞，马会叫，牛马会收到")

    def sleep(self):
        print("在牛的牛马也要睡觉")


class Student(Person):
    def study(self):
        print("努力为成为牛马学习中")


stu = Student()
stu.study()
stu.work()
stu.sleep()
print(stu.name, stu.age)
