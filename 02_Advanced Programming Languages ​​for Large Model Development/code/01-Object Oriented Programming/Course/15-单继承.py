class Animal(object):
    color = "黄"

    def __init__(self):
        self.name = "名字"
        self.__nickname = "二狗子"

    def __eat_fish(self):
        print("偷偷的说，我喜欢吃鱼")

    def eat(self):
        print("吃东西")

    def sleep(self):
        print("睡觉")


class Dog(Animal):
    def work(self):
        print("看家护院")


class Cat(Animal):
    def work(self):
        print("被撸")


dog = Dog()
dog.work()
dog.eat()
dog.sleep()
print(dog.name)
print(Dog.color)
# print(dog.__eat_fish())
