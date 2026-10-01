"""
电脑内存不可能100%比要被读取的文件大
为了小内存读取大文件，可以用生成器的方式，一条条对外吐内容
"""


def file_line_gen(path):
    with open(path, "r", encoding="UTF-8") as f:

        for line in f:
            # for line in f本质上等于 一次次调用 f.readline()
            # 每一次只占用1行数据的内层
            yield line.strip()  # 去掉这一行字符串开头和结尾的空白字符，通常包括换行符 \n、空格和制表符。


for line in file_line_gen("data.txt"):
    print(line)
