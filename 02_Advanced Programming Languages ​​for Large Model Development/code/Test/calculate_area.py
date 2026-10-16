"""
背景：
小李为了方便计算矩形面积，准备开发一个计算面积工具。
题目：
1.定义一个 Rectangle 类，构造方法接收数字参数 width、height 并保存为实例属性。(2分)
2.实现实例方法 area()，返回 width * height。(3分)
3.在 if __name__ == "__main__": 块中，创建 Rectangle(3, 5)，并打印其 area() 方法的返回值。(3分)
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    rect = Rectangle(3, 5)
    print(rect.area())
