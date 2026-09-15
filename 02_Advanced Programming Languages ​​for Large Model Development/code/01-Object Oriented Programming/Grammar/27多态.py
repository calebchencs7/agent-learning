class Animal:
    def speak(self):
        print("动物叫")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


# 同样的函数传不同的对象会有不同的行为
def make_noise(animal: Animal):
    """让传入的动物对象发出声音。"""
    animal.speak()


ani = Animal()
dog = Dog()
cat = Cat()

make_noise(ani)
make_noise(dog)
make_noise(cat)
