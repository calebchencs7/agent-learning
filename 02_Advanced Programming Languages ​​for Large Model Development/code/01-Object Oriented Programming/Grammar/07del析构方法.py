import time


class Cat:

    def __init__(self):
        print("哈基米被创建了")

    def __del__(self):
        print("哈基米被销毁了")


cat = Cat()
del cat

time.sleep(3)
