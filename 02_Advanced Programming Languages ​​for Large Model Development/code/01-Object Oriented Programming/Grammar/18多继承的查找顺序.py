
class A:
    def run(self):
        print("A run")

class B:
    def run(self):
        print("B run")

class C:
    def run(self):
        print("C run")

class D(A, B, C):
    pass

d = D()
d.run()