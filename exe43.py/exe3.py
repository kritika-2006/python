class vehicle:
    def start(self):
        print("Car start")
class car(vehicle):
    def start(self):
        super().start()
        print("Car started with a remote")

c1 = car()
c1.start()