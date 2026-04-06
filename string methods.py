# strings are immutable
a = "kritika!! kritika !!! "
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("! ")) #rstrip remove from the last element like space and !
print(a.replace("kritika","Batra"))
print(a.split(" "))
blogheading = "hi,how are you"
print(a.capitalize())

str1 = "Welcome"
print(len(str1))
print(len(str1.center(50)))
print(a.count("kritika"))

str1 = "Welcome to my profile !!!"
print(str1.endswith("!!!"))

print(str1.find("to"))

str1 = "WelcomeToMyConsole"
print(str1.isalnum())

print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Happy Birthday\n"
print(str1)
print(str1.isprintable())

#in code whitespace h ,so return true otherwise false
str1 = "    "
print(str1.isspace())

str2 = "To kill a bird"
print(str2.istitle()) #true if the first letter of each word  of the string is capatialized

print(str2.startswith("To"))