class A:
    def ShowA(self):
        print("A")
        # B is inherit from A
class B(A):
    def ShowB(self):
        print("B")
        # C is inherit from B
class C(B):
    def ShowC(self):
        print("C")

obj = C()
obj.ShowA()
obj.ShowB()
obj.ShowC()


