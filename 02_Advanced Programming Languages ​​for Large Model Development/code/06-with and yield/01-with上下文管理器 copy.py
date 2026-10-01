class MyClass:

    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


with MyClass() as mc:
    print(mc)

my = MyClass()
