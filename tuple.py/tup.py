tup = (2,3,4,6,7,"kritika")
print(type(tup),tup)
print(tup[0])
print(tup[1])
# negative indexing
print(tup[-2]) # length of tuple - 2

if "kritika" in tup:
    print("Yes,it is present")

# slicing
tup2 = tup[1:4]
print(tup2)