class vehicle:
    def __init__(self, brand):
        self.brand = brand

class car(vehicle):
    def __init__(self,brand,model):

        super().__init__(brand)
        self.model = model

c1 = car("Toyota", "Fortuner")
print(f"Brand: {c1.brand}, Model: {c1.model}")