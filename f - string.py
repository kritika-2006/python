letter = "Hey my name is {} and i am from {}"
country = "India"
name = "kritika"

print(letter.format(name, country))
# fstring 
print(f"Hey my name is {name} and i am from {country}")
# another method
print(f"We use f-string like this: Hey my name is{{name}} and i am from {{country}}")
price = 49.0999
txt = f"For only {price:.2f} dollars!"
print (txt)
#print(txt.format(price = 49.09999))