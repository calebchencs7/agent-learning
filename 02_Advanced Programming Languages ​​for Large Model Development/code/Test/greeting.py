"""
背景：
某培训平台需要在控制台中快速输出用户问候语。为了方便后续扩展用户信息，要求使用类来封装用户姓名和问候行为。
题目：
1.定义一个 Person 类，构造方法接收一个字符串参数 name 并保存为实例属性。(2分)
2.实现实例方法 say_hello()，用于打印问候语，格式为 Hello, {name}!。(3分)
3.在 if __name__ == "__main__": 块中，创建 Person("Boxuegu") 实例，并调用它的 say_hello() 方法打印问候语。
"""


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")


if __name__ == "__main__":
    person = Person("Boxuegu")
    person.say_hello()
