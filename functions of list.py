l = [2,4,6,89,90,76,56,"kritika",83,"Batra",True]
print(l)
# functions
# add 4 to the end of the list
l.append(1)
print(l)

# remove the element in the list
l.remove(89)
print(l)
# create a copy of the list
a = [2,3,1]
b = a.copy()
print(b)
#remove all the element from the list
a.clear()
print(a)
# Extend list a by adding elements from list [3, 4]
k = [1,2]
k.extend([3, 4])
print(k)
# Find the index of 3 in the list
n = [1,2,3]
print(n.index(3))
# Insert 2 at index 1
m = [1,2]
m.insert(1, 2)
print(m)
# Remove and return the last element in the list
c = [1,2,3]
c.pop()
print(c)
# Reverse the list order
a = [1,2,7,3,0,8]
a.reverse()
print(a)
# Sort the list in ascending order
a.sort()
print(a)