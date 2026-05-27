class A:
    def showA(self):
        print("A")
        # B is inherit from A
class B:
    def showB(self):
        print("B")
        # C is inherit from the A and B
class C(A,B):
    def showC(self):
        print("C")
obj = C()
obj.showA()
obj.showB()
obj.showC()