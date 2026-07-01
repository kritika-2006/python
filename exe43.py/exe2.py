class vehicle:
    def start(self):
        print("Vehicle started")
class car (vehicle):
    def start(self):
        print("Car started with a Remote!")
c1 = car()
c1.start()
