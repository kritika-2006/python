class Phone:
    def call(self):
        print("Calling...")
class SmartPhone(Phone):
    def take_Photo(self):
        print("Click! Photo captured")
sp = SmartPhone()
sp.take_Photo()
sp.call()