s1 = {1,2,5,6}
s2 = {3,4,6,7,9}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

k1 = {3,4,5,6}
k2 = {5,9,0,1}
k3 = k1.intersection(k2)
print(k3)

d1 = {"kolkata", "delhi",4,5,1,3}
d2 = {"london","america",3,1}
d3 = d1.symmetric_difference(d2)
print(d3)

f1 = {"kritika",7,8,9}
f2 = {8,9,5,3,0}
f3 = f1.difference(f2)
print(f3)

w1 = {"london","france",3,6,7}
w2 = {"rohtak",3,9,0,1,6}
w3 = w1.isdisjoint(w2) # dijoint means same element in both set
print(w3)

q1 = {"london","karnatka",8,9,0}
q2 = {"london","kritika",6,9,3,2}
print( q1.issuperset(q2)) #superset means q2 superset tab hoga jab q1 ma q2 ka sae elements present honge
q3 = {"london",8,9,0}
print(q1.issuperset(q3))
print(q3.issubset(q1))

e= {"apple","mango","banana","orange"}
e.add("litchi")
print(e)
e.remove("orange")
print(e)