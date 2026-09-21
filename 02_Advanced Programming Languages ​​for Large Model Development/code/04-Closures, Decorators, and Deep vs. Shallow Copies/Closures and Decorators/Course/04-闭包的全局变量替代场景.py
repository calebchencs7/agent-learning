# counter1 = 0
# counter2 = 0
def counter():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        print(f"counter: {counter}")

    return inner


def work1(f):
    print("我爱工作，工作使我快乐！请计件")
    f()


def work2(f):
    print("黑马程序员真棒，野得很太好了（PS：请计件）")
    f()


print("开始招募水军了")
f1 = counter()
f2 = counter()

work1(f1)
work2(f2)

work1(f1)
work2(f2)

work1(f1)
work2(f2)
