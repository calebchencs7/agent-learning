# 1. 创建一个类 Animal， 里面提供eat方法  内容随意
# 2. 创建一个类Dog 继承Animal，并对父类的eat进行复写，内容随意
# 3. 在Dog类中，提供super_eat()方法，在方法内调用父类的eat方法
class Animal:
    def eat(self):
        print("动物吃")


class Dog(Animal):
    def eat(self):
        print("狗吃")

    def super_eat(self):
        # Animal.eat(self)
        super().eat()


dog = Dog()
dog.eat()
dog.super_eat()
