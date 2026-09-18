def eat():
    print("吃")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

   

    @staticmethod
     """静态方法就是：逻辑上属于某个类，但不需要使用对象数据或类数据的工具函数。"""
    def say_hi(self):
        print(f"大家好真的狗{self.name}, 今年{self.age}岁")

    @staticmethod
    def eat():
        print("吃")


#普通函数调用
eat()

d = Dog
# 静态的调用，可以用类名调用
Dog.eat()
# 静态的调用，可以用对象调用
d.eat()
