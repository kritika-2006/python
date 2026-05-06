class Person:
    # constructor
    def __init__(self): # default constructor (no arguments pass)
        print("Hey I am a Person")
a = Person()

# constructor with arguments (parametrised constructor)
class Office:
    def __init__(self, name , occ):
        print("Hi, I am  working as Analyst")
        self.name = name
        self.occ = occ

    def info(self):
         print(f"{self.name} is a {self.occ}")

a = Office("Kritika" , "Cyber Security Analyst")
b = Office("Sunita","HR")
a.info()
b.info()
        