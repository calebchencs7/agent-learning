# 需求: 假设正常工作18-100岁,打印:xx岁了,正在工作
# 条件是:当天年龄是65岁,退休,享受老年生活了
age = 18
while age < 101:
    if age == 65:
        print('65退休了,享受老年生活了')
        break
    print(f"{age}岁了,正在工作...")
    age += 1

print('====================')

for age in range(18, 101):
    if age == 65:
        print('65退休了,享受老年生活了')
        break
    print(f"{age}岁了,正在工作...")
