# 1. 设计一个Dog class，记录name和food 2个字符串变量
class Dog:
    name = None
    food = None

    def say_hi(self):
        print(f"我是{self.name}，我吃{self.food}")
# 2. 在Dog类设计一个方法（函数）say_hi，打印dog的name和food，我是xxx，我吃xxx
# 要注意self这个新关键字
#
# 3. 创建2个Dog对象（变量）
dog1 = Dog()
dog2 = Dog()
# 4. 给2个对象存入对应的name和food值
dog1.name = "大黄"
dog1.food = "面包"

dog2.name = "阿黄"
dog2.food = "米饭"
# 5. 调用2个对象各自的 say_hi方法

dog1.say_hi()
dog2.say_hi()
