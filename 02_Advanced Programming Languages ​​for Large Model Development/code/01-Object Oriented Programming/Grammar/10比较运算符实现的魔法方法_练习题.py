class Dog:
    """设计一个Dog类，有2个成员属性，姓名、年龄"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        """要求return bool值"""
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name


# 创建Dog类的2个类对象
dog1 = Dog("大黄", 11)
dog2 = Dog("大黄", 11)
# 2. 要求2个类对象可以用 > 符号实现年龄比较
print(dog1 > dog2)
# 3. 要求2个类对象可以用 ==符号，实现姓名是否相等
# 如果不实现 __eq__ 则 == 默认比较内存地址
print(dog1 == dog2)
