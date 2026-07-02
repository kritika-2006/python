class vehicle:
    def info(self):
        print("I am a vehicle")
class car(vehicle):
    def car_info(self):
        print("I am a car")
class ElectricCar(car):
    def battery_info(self):
        print("I have a 60kwh battery")

ec = ElectricCar()
ec.battery_info()
ec.car_info()
ec.info()
