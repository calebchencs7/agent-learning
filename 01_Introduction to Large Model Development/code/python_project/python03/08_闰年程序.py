# 小明想编写一个程序，通过输入年份来判断是否为闰年。
# 如果年份能被400整除，则为闰年；如果年份能被4整除但不能被100整除也为闰年
year = int(input("Please enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
