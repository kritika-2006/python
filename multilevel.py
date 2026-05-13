class A:
    def ShowA(self):
        print("A")
class B(A):
    def ShowB(self):
        print("B")
class C(B):
    def ShowC(self):
        print("C")
        # object
obj = C()
obj.ShowA()
obj.ShowB()
obj.ShowC()


