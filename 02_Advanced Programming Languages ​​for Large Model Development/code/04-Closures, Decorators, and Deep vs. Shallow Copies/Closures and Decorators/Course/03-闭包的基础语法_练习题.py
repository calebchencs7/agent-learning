# 1. 通过闭包，实现对变量info字符串的保存


def bibao():

    info = "我是周杰轮，给我打钱"

    # 内外双嵌套函数
    def neibu():
        # 内层使用了外层变量
        print(info)

    # 外层返回内层函数本身
    return neibu


# f变量就是 内部函数本身
# 由于内部函数需求外部的info，为了支持f可以正常用，info被记录到f内部
f = bibao()

f()
f()
f()
