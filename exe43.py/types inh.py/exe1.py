class vehicle:
    def info(self):
        print("This is a wallet")
class car(vehicle):
    def car_info(self):
        print("This is a car")
class ElectricCar(car):
    def battery_info(self):
        print("Electric car has battery power")

ec = ElectricCar()
ec.info()
ec.car_info()
ec.battery_info()