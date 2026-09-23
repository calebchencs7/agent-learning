# 练习1
# 给定字符串：my_tel1 = "tel:13812345678"
# 使用 re.sub，把里面所有数字替换成 *
import re
my_tel1 = "tel:13812345678"

print(re.sub(r"\d", "*", my_tel1))

# 练习2
# 给定字符串：ip = "192.168.1.25"
# 使用 re.sub，把所有的点 . 替换成短横线 -
ip = "192.168.1.25"
print(re.sub(r"\.", "-", ip))
# 3. 将第二个需求改为，仅替换第一个.
ip = "192.168.1.25"
print(re.sub(r"\.", "-", ip, count=1))
