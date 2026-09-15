# 需求: 夜深人静的时候,你一个人正常坐20层楼的电梯,每一层都要报"x层到了~"
# 条件: 不想听到4,14,18层到了
for i in range(1, 21):
    if i == 4 or i == 14 or i == 18:
        continue
    print(f"{i}层到了~")

print('=========================')

i = 0
while i < 20:
    i += 1
    if i == 4 or i == 14 or i == 18:
        continue
    print(f"{i}层到了~")
