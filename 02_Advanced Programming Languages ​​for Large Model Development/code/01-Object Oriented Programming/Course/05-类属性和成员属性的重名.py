
class Dog:
    name = "狗子"

    def __init__(self, name):
        self.name = name

dog1 = Dog("好狗")
dog2 = Dog("懒狗")

print(dog1.name)
print(dog2.name)

print(Dog.name)

"""
类属性访问：      类名.属性名
类属性修改：      类名.属性名 = 值
成员属性访问：     对象名.属性名
成员属性修改：     对象名.属性名 = 值
"""
