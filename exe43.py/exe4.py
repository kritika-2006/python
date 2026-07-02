class vehicle:
    def __init__(self,brand):
        self.brand = brand

class Car(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model

c1 = Car("Tata" , "Nexon")
print(c1.brand, c1.model) 