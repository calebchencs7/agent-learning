"""
and: 并且  有假则假
or: 获取  有真则真
not: 取反
"""

# and: 并且  有False则False
print("and")
print(True and True)
print(True and False)
print(False and False)

# or: 获取  有True则True
print("or")
print(True or True)
print(True or False)
print(False or False)

# not: 取反
print("not ")
print(not True)
print(not False)
print("=======================================")

# 示例:
print(10 < 5 and 1 > 3)
print(10 < 5 or 1 > 3)
print(not 1 > 3)
