class Student:
    # less than 小于
    # greater than 大于
    # equal 等于
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def lt_by_height(self, other):
    #     return self.height < other.height

    def __lt__(self, other):  # less than 小于比较
        """self 是比较的发起者，other 被比较的另一个，比较小于"""
        # 当类对象使用<符号和它人比较，会自动查找__lt__方法执行做比较，被比较的other会自动传入此方法
        print("要比较小于了")
        return self.age < other.age

    def __gt__(self, other):  # greater than  大于比较
        print("要比较大于了")
        return self.age > other.age

    def __le__(self, other):  # less equal    小于等于比较
        print("要比较 <=")
        return self.age <= other.age

    def __ge__(self, other):  # greater equal  大于等于比较
        print("要比较 >=")
        return self.age >= other.age

    def __eq__(self, other):  # equal  相等
        print("要比较 ==")
        return self.age == other.age

    def __ne__(self, other):  # not equal 不相等
        print("要比较 !=")
        return self.age != other.age


stu1 = Student("狗子", 11)
stu2 = Student("猫子", 3)

print(stu1 > stu2)
print(stu1 < stu2)
print(stu1 >= stu2)
print(stu1 <= stu2)
print(stu1 == stu2)
print(stu1 != stu2)

# stu1.lt_by_height(stu2)
# print(type(3))
# if 2 < 5:
#     print("5大")
# else:
#     print("2大")
