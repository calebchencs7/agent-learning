
class Animal(object):
    def eat(self):
        print("吃")


class Person(Animal):
    def sleep(self):
        print("睡")


class Worker(Person):
    def work(self):
        print("工作")


class Student(Person):
    def study(self):
        print("学习")

animal = Animal()
animal.eat()

person = Person()
person.eat()
person.sleep()

worker = Worker()
worker.eat()
worker.sleep()
worker.work()

student = Student()
student.eat()
student.sleep()
student.study()
