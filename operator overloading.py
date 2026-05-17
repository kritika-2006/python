class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return point (new_x,new_y)
    def __repr__(self):
       return f"Point({self.x}, {self.y})"
P1 = point(1,2)
P2 = point(2,1)
P3 = P1+P2
print(P3)   

