class Laptop:
    def start(self):
        print("Laptop starting with a Power button")

class Phone:
    def start(self):
        print("Phone starting with a side button")

def boot_device(device):
    device.start()

l1 = Laptop()
p1 = Phone()

boot_device(l1)
boot_device(p1)
