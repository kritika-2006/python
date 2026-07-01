class vehicle:
    def start(self):
        print("Vehicle Started")
class car(vehicle):
        def honk(self):
             print("Beep Beep")

c1 = car()
c1.start()
c1.honk()