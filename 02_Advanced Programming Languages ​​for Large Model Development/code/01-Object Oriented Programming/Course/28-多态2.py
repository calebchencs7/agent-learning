# 一个对象（行为），多种工作状态


class Animal:
    def work(self):
        print("动物在干活")


class Person(Animal):
    def work(self):
        print("牛马工作")


class Student(Person):
    def study(self):
        print("俺在学习")


def work(obj: Animal):
    obj.work()


p = Person()
a = Animal()
s = Student()
work(p)
work(a)
work(s)
