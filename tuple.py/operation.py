# tuples are immutable
# in tuple we don't add or remove the element in directly
tup = ("spain","russia","india","New york","Assia")
temp = list(tup)
temp.append("Australia") # add item
temp.pop(3) # remove item 
temp[2] = "Canada" # change item 
tup = tuple(temp)
print(tup)

m = (0,3,5,89,67,2)
res = m.count(2)
r = len(m)
print(len(m))
print("count of 2 in m is:",res)
# slicing
n = (2,4,6,7,9,3,1,90,56)
res = n.index(3,4,8)
print("count of 3 in n is:",res)

