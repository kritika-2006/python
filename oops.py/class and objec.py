# class
class Person:
    name = "kritika"
    occupation = "Cyber security"
    networth = 10

    def info(self):
        # self is used to access the current instance of the class
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()
# object
a.name = "ritika"
a.occupation = "Software Engineer"

b.name = "kirti"
b.occupation = "HR"

a.info()
b.info()
c.info()