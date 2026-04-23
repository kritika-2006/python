# combination of key- values pair
dict = {
    1 : "kritika",
    "city" : "Sonipat"
}
print(dict[1])
print(dict["city"])
print(dict)
# when key is not exist in dictionary so,print none
#print(dict["name"])  show error
print(dict.get("name")) # show none

# all values iterate
for key in dict.keys():
    print(f"The value corresponding to the key {key} is {dict[key]}")
