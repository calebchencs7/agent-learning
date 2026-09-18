class OldProgrammer:
    def programming(self):
        print("古法编程。纯手搓，100%无AI添加")


class NewProgrammer(OldProgrammer):
    def programming(self):  # 对父类成员方法的重写
        print("纯AI编程，拒绝古法手搓")


np = NewProgrammer()
np.programming()
