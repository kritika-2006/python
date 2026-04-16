l = [1,2,"kritika",True , 6, 7, 43, 45,67,78]
print(l)
print(type(l))
print(l[2])
# negative indexing
# when negative indexing is using then first convert to positive indexing

print(l[-3])
# explanation
print(l[len(l)-3])

if "kritika" in l:
    print("Yes")
else:
    print("No")

#same
print(l[1:-2])
print(l[1:3]) # length - 2

# jumping index concept
print(l)
print(l[1:8])
print(l[1:8:3]) # 3 baar jump hoga 
