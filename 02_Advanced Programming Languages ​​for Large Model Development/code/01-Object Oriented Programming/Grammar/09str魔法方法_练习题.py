# 设计一个Dog类，有3个成员属性，姓名、颜色、年龄
# 创建Dog类的一个类对象
# 要求，print输出类对象的时候结果是
# 我是xxx狗子，颜色xxx，今年xxx岁
import time


class Dog(object):

    def __init__(self, name, color, age):
        print("创建了狗子")
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        print("str方法被调用了")
        return f"我是{self.name}狗子，颜色{self.color}，今年{self.age}岁"


dog = Dog("大黄", "黄色", 2)
time.sleep(3)
print(dog)

# print：将内容作为字符串输出
