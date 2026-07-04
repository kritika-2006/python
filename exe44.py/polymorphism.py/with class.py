class cat:
    def speak(self):
        print("Meow Meow")
class dog:
    def speak(self):
        print("Woof Woof")

def animal_sound(animal_object):
    animal_object.speak()

c1 = cat()
d1 = dog()

animal_sound(c1)
animal_sound(d1)