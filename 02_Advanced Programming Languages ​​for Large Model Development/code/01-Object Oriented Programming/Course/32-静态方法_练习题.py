# 1. 写一个类Cat，里面提供一个静态方法叫做hello
# 2. 静态方法里面print一句话，内容随意
#
# 3. 使用类名称调用静态方法
# 4. 创建Cat类对象，用类对象调用静态试试

class Cat:

    @staticmethod
    def hello():
        print("大家好，我是哈基米")


Cat.hello()

cat = Cat()
cat.hello()

