class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def code(self):
        print("Developer is writing Python code")

d1 = Developer()
d1.work()
d1.code()
print(isinstance(d1,Developer)) # kya d1 Developer ka object h ?
print(issubclass(Developer, Employee)) # kya developer Employee ki child class h ?
print(issubclass(Employee,Developer)) # same