class student:
    def __init__(self,name,marks):
       self.name = name
       self.marks = marks
    def check_result(self):
        if self.marks >= 40:
            print("Congratulations! you are passed.")
        else:
            print("Fail.")

# object
s1 = student("kritika",95)
# call function
s1.check_result()