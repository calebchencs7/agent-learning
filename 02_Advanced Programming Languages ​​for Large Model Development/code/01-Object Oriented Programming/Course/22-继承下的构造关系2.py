class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Dog(Animal):
    def __init__(self, name, color, age):
        self.age = age
        super().__init__(name, color)

dog = Dog("小黄", "黑", 11)
print(dog.name)
print(dog.color)
print(dog.age)