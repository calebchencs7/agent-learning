def eat():
    print("吃")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def say_hi():
        """静态方法就是：逻辑上属于某个类，但不需要使用对象数据或类数据的工具函数。"""
        print("大家好，我是一只狗")

    @staticmethod
    def eat():
        print("吃")


# 普通函数调用
eat()

# 静态方法可以通过类名调用
d = Dog("旺财", 3)
Dog.say_hi()
Dog.eat()

# 静态方法也可以通过对象调用
d.say_hi()
d.eat()
