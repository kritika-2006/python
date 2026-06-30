class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def introduce(self):
        print(f"hi,mera name {self.name}")
    
s1 = student("kritika",95)
s1.introduce()
print(s1.marks)