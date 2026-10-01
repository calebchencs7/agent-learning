"""
写一个类，提供一个random_line方法，调用向文件添加随机内容
"""

import random
import time


class MyClass(object):
    def __init__(self, path):
        self.file = open(path, 'a+', encoding='utf-8')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('即将退出，关闭文件')
        self.file.close()

    def random_line(self):
        lines = [
            '人生苦短，我用Python',
            'Python是最好的语言',
        ]

        self.file.write(random.choice(lines) + '\n')


with MyClass('test.txt') as mc:
    for _ in range(5):
        mc.random_line()
