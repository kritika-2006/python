class father:
    def house(self):
        print("Father house")
class Mother:
    def car(self):
        print("Mother car")
class son(father,Mother):
    def bike(self):
        print("Son bike")
class GrandSon(son):
    def cycle(self):
        print("Grandson cycle")
obj = GrandSon()
obj.house()
obj.car()
obj.bike()
obj.cycle()
