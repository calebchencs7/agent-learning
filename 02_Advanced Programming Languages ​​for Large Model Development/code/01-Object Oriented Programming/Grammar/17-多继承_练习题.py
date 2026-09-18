# 设计一个Animal类提供一个eat方法
# 2. 设计一个 Worker类提供 work方法
#
# 3. 设计一个 Student类提供study方法
#
# 4. 设计一个 Me 类，继承上面3个类
# 类的内容是pass


class Animal:
    def eat(self):
        print("I am eating")


class Worker:
    def work(self):
        print("I am working")


class Student:
    def study(self):
        print("I am studying")


class Me(Animal, Worker, Student):
    pass


me = Me()
me.eat()
me.work()
me.study()
