class Student:
    def __init__(self,name,course,marks):
        self.name = name
        self.course = course
        self.marks = marks

s1 = Student("kritika","B.tech",95)

print(f"{s1.name} is studying {s1.course} and scored {s1.marks} marks.")