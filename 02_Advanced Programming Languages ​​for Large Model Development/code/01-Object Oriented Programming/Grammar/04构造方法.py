class Dog(object):
    color = "黑"
    # 1. __init__ 在创建类对象的时候自动调用
    # 2. 在创建类对象的时候传入的参数，会自动传给__init__

    def __init__(self, name, food, age):
        # 设置3个成员属性
        self.name = name  # self代表类对象本身
        self.food = food
        self.age = age


dog1 = Dog("大黄", "面条", 2)
print(dog1.name, dog1.age, dog1.food, dog1.color)
dog2 = Dog("小黄", "米饭", 1)
print(dog2.name, dog2.age, dog2.food, dog2.color)
print("-" * 20)

# 成员属性的修改
dog1.food = "馒头"
dog2.food = "披萨"
print(dog1.name, dog1.age, dog1.food, dog1.color)
print(dog2.name, dog2.age, dog2.food, dog2.color)

# 类属性的修改
print("-" * 20)
Dog.color = "白"

print(dog1.name, dog1.age, dog1.food, dog1.color)
print(dog2.name, dog2.age, dog2.food, dog2.color)
