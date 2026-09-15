class OldProgrammer:
    def programming(self):
        print("古法编程。纯手搓，100%无AI添加")


class NewProgrammer(OldProgrammer):
    def programming(self, use_old_school=False):  # 对父类成员方法的复写
        if use_old_school:
            # 方式1 父类名.方法(self)   self自己填
            # OldProgrammer.programming(self)

            # 方式2 super().方法
            super().programming()
        else:
            print("纯AI编程，拒绝古法手搓")

    def baba_programming(self):
        super().programming()


np = NewProgrammer()
# np.programming(True)
np.baba_programming()
