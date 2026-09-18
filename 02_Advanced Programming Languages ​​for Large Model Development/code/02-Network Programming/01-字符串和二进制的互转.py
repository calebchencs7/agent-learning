# encode 编码 -> 字符串转二进制
name = "周"
name_byte = name.encode("UTF-8")
print(name_byte, type(name_byte))
# decode 解码 -> 二进制转字符串

name2 = name_byte.decode("UTF-8")
print(name2)


# UTF8
# 周 -> \xe5\x91\xa8 -> 1110 0101 1001 0001 1010 1000
# 1个二进制1个bit，8个二进制 1个byte
# 在UTF8 一个中文转为3个byte（24个二进制）

# GBK
# GBK 一个中文占用2个byte，16个二进制数字
# 周 -> 10001111 11111111

# 1byte = 8bits
# 1024 byte = 1KB
# 1024KB = 1MB
# 1024MB = 1GB
