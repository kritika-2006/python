class Father:
    def skill_f(self):
        print("Father loves Gardening")
class Mother:
    def skill_m(self):
        print("mother loves coding")
class child(Father,Mother):
    def my_skill(self):
        print("I love music")

c = child()
c.skill_f()
c.skill_m()
c.my_skill()