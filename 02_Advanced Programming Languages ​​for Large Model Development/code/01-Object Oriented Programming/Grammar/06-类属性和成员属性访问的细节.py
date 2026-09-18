
class Dog:
    name = "狗子"

    def __init__(self, age):
        print("我被执行了")
        self.age = age

dog1 = Dog(11)
dog2 = Dog(12)
print(dog1.name)        # 如果成员属性不存在，去访问同名类属性
# print(dog1.food)        # 成员属性和类属性都不存在，那访问不了，报错

dog1.name = "大黄"        # 成员属性不存在，新建成员属性
print(dog1.name)        #  dog1已经新建了name成员属性 所以结果是大黄
print(dog2.name)        # dog2没有name成员属性，访问同名的类属性去了
