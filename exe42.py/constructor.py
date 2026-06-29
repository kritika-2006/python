class Student:
    # 'self' ka matlab hai jo naya student object ban raha hai
    def __init__(self, name_param, roll_param):
        self.name = name_param
        self.roll = roll_param

# Bracket ke andar hi data bhej diya
s1 = Student("Kritika", 101)

print(s1.name)
print(s1.roll)