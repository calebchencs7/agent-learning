# Method Resolution Order
class A:
    def __init__(self, name):
        print("A init")


class B(A):
    def __init__(self, name, age):
        print("B init")
        super().__init__(name)


class C(B):
    def __init__(self, name, age):
        print("C init")
        super().__init__(name, age)


class Dog(C):
    def __init__(self, name, age):
        print("Dog init")
        super().__init__(name, age)


# print(Dog.__mro__)      Dog -> C -> B -> A -> object
dog = Dog("大黄", 11)
