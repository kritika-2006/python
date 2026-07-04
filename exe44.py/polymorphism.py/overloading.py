class Area:
    # overloading None or default arguments ka sath hota h 
    def calculate(self,l,b=None): 
        if b is not None:
            print("Area of Rectangle:", l * b)
        else:
            print("Area of Square:", l * l)

a1 = Area()
a1.calculate(3)
a1.calculate(5,10)
            
    