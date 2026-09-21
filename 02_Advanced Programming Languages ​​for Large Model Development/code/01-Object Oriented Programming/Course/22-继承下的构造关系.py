class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Dog(Animal):
    pass


dog = Dog("大黄", "黄")
print(dog.name, dog.color)

print(Dog.__mro__)
