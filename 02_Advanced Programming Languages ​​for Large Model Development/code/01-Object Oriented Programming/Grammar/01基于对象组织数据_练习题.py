# 1. 设计一个Dog的类 记录name和age
class Dog:
    name = None
    age = None
# 2. 通过设计好的类创建2个Dog的对象
dog1 = Dog()
dog2 = Dog()
# 3. 给2个Dog对象分别存入对应的数据
dog1.name = "大黄"
dog1.age = 3

dog2.name = "小美"
dog2.age = 2
# 4. print输出显示2个Dog对象存入的信息
print(f"dog1是{dog1.name}, 年龄：{dog1.age}岁")
print(f"dog2是{dog2.name}, 年龄：{dog2.age}岁")
